-- Verify stainless:appschema on pg

BEGIN;

DO $$
BEGIN
    ASSERT (SELECT has_schema_privilege('stainless', 'usage'));
END $$;

ROLLBACK;
