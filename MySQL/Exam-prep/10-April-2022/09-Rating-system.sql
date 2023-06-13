SELECT 
    title,
    (IF(rating <= 4,
        'poor',
        IF(rating <= 7, 'good', 'excellent'))) AS rating,
    (IF(has_subtitles = 1, 'english', '-')) AS subtitles,
    budget
FROM
    movies_additional_info AS mai
        JOIN
    movies AS m ON m.movie_info_id = mai.id
ORDER BY budget DESC;