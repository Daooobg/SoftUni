SELECT 
    name
FROM
    towns
WHERE
    CHAR_LENGTH(name) BETWEEN 5 AND 6
ORDER BY name;