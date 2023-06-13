SELECT 
    mai.id AS id,
    m.title AS title,
    mai.runtime AS runtime,
    mai.budget AS budget,
    mai.release_date AS release_date
FROM
    movies_additional_info AS mai
        JOIN
    movies AS m ON m.movie_info_id = mai.id
WHERE
    YEAR(mai.release_date) BETWEEN 1996 AND 1999
ORDER BY mai.runtime , mai.id
LIMIT 20;