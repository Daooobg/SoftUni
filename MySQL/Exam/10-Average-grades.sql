DELIMITER $$
CREATE FUNCTION udf_average_alumni_grade_by_course_name(course_name VARCHAR(60))
RETURNS DECIMAL(19, 2)
DETERMINISTIC
BEGIN
	RETURN (SELECT AVG(sc.grade) FROM courses AS c
			JOIN students_courses AS sc ON sc.course_id = c.id
			JOIN students AS s ON s.id = sc.student_id
			WHERE c.name = course_name AND s.is_graduated = 1);
END $$

DELIMITER ;
;

SELECT c.name, udf_average_alumni_grade_by_course_name('Quantum Physics') as average_alumni_grade FROM courses c 
WHERE c.name = 'Quantum Physics';


SELECT AVG(sc.grade) FROM courses AS c
JOIN students_courses AS sc ON sc.course_id = c.id
JOIN students AS s ON s.id = sc.student_id
WHERE c.name = 'Quantum Physics' AND s.is_graduated = 1;

SELECT * FROM courses AS c
JOIN students_courses AS sc ON sc.course_id = c.id
JOIN students AS s ON s.id = sc.student_id
WHERE c.name = 'Quantum Physics' AND s.is_graduated = 1