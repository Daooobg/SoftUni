DELETE FROM countries AS c
WHERE (SELECT COUNT(*) FROM movies WHERE country_id = c.id) = 0;