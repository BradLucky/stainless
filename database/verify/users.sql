-- Verify stainless:users on pg

BEGIN;

SELECT id, first_name, last_name, password
FROM stainless.users
WHERE FALSE;

ROLLBACK;
