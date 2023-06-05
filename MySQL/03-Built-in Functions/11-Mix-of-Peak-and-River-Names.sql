SELECT 
    peaks.peak_name,
    rivers.river_name,
    LOWER(CONCAT(peaks.peak_name,
                    SUBSTRING(rivers.river_name, 2))) AS mix
FROM
    peaks,
    rivers
WHERE
    LEFT(rivers.river_name, 1) = RIGHT(peaks.peak_name, 1)
ORDER BY mix;