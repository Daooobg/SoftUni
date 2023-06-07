SELECT 
    COUNT(*) AS country_code
FROM
    countries AS c
        LEFT JOIN
    mountains_countries AS mc ON mc.country_code = c.country_code
WHERE
    mc.mountain_id IS NULL;
