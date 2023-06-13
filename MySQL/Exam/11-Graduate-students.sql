DELIMITER $$
CREATE PROCEDURE udp_graduate_all_students_by_year(year_started INT)
BEGIN
	UPDATE courses AS c
		JOIN students_courses AS sc ON sc.course_id = c.id
		JOIN students AS s ON s.id = sc.student_id
		SET is_graduated = 1
		WHERE YEAR(start_date) = year_started ;
	
END$$

DELIMITER ;
;

CALL udp_graduate_all_students_by_year(2017);

SELECT * FROM courses AS c
JOIN students_courses AS sc ON sc.course_id = c.id
JOIN students AS s ON s.id = sc.student_id
WHERE YEAR(start_date) = 2017 