-- Verify stainless:users on pg

BEGIN;

SELECT id, name, password
FROM stainless.users
WHERE FALSE;

ROLLBACK;
