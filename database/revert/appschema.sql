-- Revert stainless:appschema from pg

BEGIN;

DROP SCHEMA stainless;

COMMIT;
