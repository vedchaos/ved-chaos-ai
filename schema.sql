-- Ved Chaos AI - Cloud PostgreSQL Memory Schema
-- Supports Full-Text Search (FTS), pgvector HNSW embeddings, deduplication, and RLS defense.

CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS vector;

-- 1. User Profiles Store
CREATE TABLE IF NOT EXISTS user_profiles (
    user_id TEXT PRIMARY KEY,
    profile_json JSONB NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Trigger to keep updated_at in sync
CREATE OR REPLACE FUNCTION update_user_profiles_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_user_profiles_updated_at ON user_profiles;
CREATE TRIGGER trg_user_profiles_updated_at
    BEFORE UPDATE ON user_profiles
    FOR EACH ROW
    EXECUTE FUNCTION update_user_profiles_updated_at();

-- 2. Chat & Memory Examples (Hybrid FTS + pgvector)
CREATE TABLE IF NOT EXISTS chat_examples (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
    content TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    source_label TEXT DEFAULT 'chat',
    embedding vector(1536),
    content_tsv tsvector GENERATED ALWAYS AS (to_tsvector('simple', content)) STORED,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    CONSTRAINT chat_examples_user_content_hash_uniq UNIQUE (user_id, content_hash)
);

-- Compound Index for chronological user memory retrieval
CREATE INDEX IF NOT EXISTS chat_examples_user_created_idx
    ON chat_examples (user_id, created_at DESC);

-- GIN Index on Generated tsvector column for instant keyword matching
CREATE INDEX IF NOT EXISTS chat_examples_content_tsv_idx
    ON chat_examples USING GIN (content_tsv);

-- HNSW Vector Index for cosine similarity searches
CREATE INDEX IF NOT EXISTS chat_examples_embedding_hnsw_idx
    ON chat_examples USING hnsw (embedding vector_cosine_ops);

-- 3. Row Level Security (RLS) - Hardened for Supabase/Neon PostgREST exposure
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE chat_examples ENABLE ROW LEVEL SECURITY;

-- Note: In production Supabase/Neon, create policies matching your auth provider.
-- For server-side service keys or direct PostgreSQL connections, RLS is bypassed by superuser/service_role.
