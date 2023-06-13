SELECT 
    CONCAT(a.first_name, ' ', a.last_name) AS full_name,
    CONCAT(REVERSE(a.last_name),
            CHAR_LENGTH(a.last_name),
            '@cast.com'),
    2022 - YEAR(a.birthdate) AS age,
    a.height AS height
FROM
    movies_actors AS ma
        RIGHT JOIN
    actors AS a ON a.id = ma.actor_id
WHERE
    ma.actor_id IS NULL
ORDER BY height;