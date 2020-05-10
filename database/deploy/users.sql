-- Deploy stainless:users to pg
-- requires: appschema

BEGIN;

SET client_min_messages = 'warning';

CREATE TABLE stainless.users (
    id         SERIAL      PRIMARY KEY,
    name       TEXT        NOT NULL,
    email      TEXT        NOT NULL,
    password   TEXT        NOT NULL,
    created_ts TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMIT;
