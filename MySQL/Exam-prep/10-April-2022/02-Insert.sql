INSERT INTO actors (first_name, last_name, birthdate, height, awards, country_id)
	(
    SELECT 
		REVERSE(first_name),
        REVERSE(last_name),
        DATE_SUB(birthdate, INTERVAL 2 DAY),
        height + 10,
        country_id,
        (SELECT id from countries as c WHERE c.name = 'Armenia')
        FROM actors
        WHERE actors.id <= 10
    );
SELECT * FROM actors AS a
JOIN countries AS c ON a.country_id = c.id
WHERE a.first_name = 'adniL'  ;