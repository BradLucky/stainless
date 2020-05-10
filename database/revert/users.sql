-- Revert stainless:users from pg

BEGIN;

DROP TABLE stainless.users;

COMMIT;
