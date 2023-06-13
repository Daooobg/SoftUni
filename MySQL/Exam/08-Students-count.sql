SELECT 
    COUNT(*) AS students_count, u.`name` AS university_name
FROM
    universities AS u
        JOIN
    courses AS c ON c.university_id = u.id
        JOIN
    students_courses AS sc ON sc.course_id = c.id
GROUP BY university_name
HAVING students_count >= 8
ORDER BY students_count DESC , university_name DESC;
