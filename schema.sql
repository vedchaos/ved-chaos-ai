CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS user_profiles (
    user_id TEXT PRIMARY KEY,
    profile_json JSONB NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS chat_examples (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('user', 'assistant')),
    content TEXT NOT NULL,
    source_label TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS chat_examples_user_created_idx
    ON chat_examples (user_id, created_at DESC);

CREATE INDEX IF NOT EXISTS chat_examples_fts_idx
    ON chat_examples USING GIN (to_tsvector('simple', content));

-- IMPORTANT:
-- This starter app scopes every query to VED_USER_ID in the server environment.
-- Do not expose the database directly to clients. If multiple users will use this,
-- add real authentication, per-user authorization, and database Row Level Security (RLS).
