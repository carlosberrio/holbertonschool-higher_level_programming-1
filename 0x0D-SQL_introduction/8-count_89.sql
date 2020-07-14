-- Script that displays the number of records with id = 89 in the table first_table of a database in a MySQL server.
-- The database name will be passed as an argument of the mysql command.

SELECT COUNT(id) FROM first_table WHERE id=89;
