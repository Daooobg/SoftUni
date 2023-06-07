SELECT 
    mc.country_code, COUNT(country_code) AS mountain_range
FROM
    mountains AS m
        JOIN
    mountains_countries AS mc ON m.id = mc.mountain_id
WHERE
    mc.country_code IN ('BG' , 'RU', 'US')
GROUP BY mc.country_code
ORDER BY mountain_range DESC;