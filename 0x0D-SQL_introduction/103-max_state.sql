-- Script that displays the max temperature of each state (ordered by State name).
-- SQL is cool.

SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
