# NovaRestoreCheck

Validate a PostgreSQL custom-format dump with `novarestorecheck BACKUP.dump`. It runs `pg_restore --list` and reports whether PostgreSQL can read the archive catalog. It does not restore or modify a database. Requires PostgreSQL client tools.
