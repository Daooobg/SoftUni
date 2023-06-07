SELECT 
    country_name,
    MAX(p.elevation) AS highest_peak_elevation,
    MAX(r.length) AS longest_river_length
FROM
    countries AS c
        LEFT JOIN
    countries_rivers AS cr ON cr.country_code = c.country_code
        LEFT JOIN
    rivers AS r ON cr.river_id = r.id
        LEFT JOIN
    mountains_countries AS mc ON mc.country_code = c.country_code
        LEFT JOIN
    peaks AS p ON p.mountain_id = mc.mountain_id
GROUP BY country_name
ORDER BY highest_peak_elevation DESC , country_name
LIMIT 5;