-- Deploy stainless:users to pg
-- requires: appschema

BEGIN;

SET client_min_messages = 'warning';

CREATE TABLE stainless.users (
    id         SERIAL      PRIMARY KEY,
    email      TEXT        NOT NULL,
    first_name TEXT        NOT NULL,
    last_name  TEXT        NOT NULL,
    password   TEXT        NOT NULL,
    created_ts TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMIT;
