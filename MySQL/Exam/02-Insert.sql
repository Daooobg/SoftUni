INSERT INTO courses(`name`, duration_hours, start_date,  teacher_name , `description`, university_id )
	(
    SELECT 
		CONCAT(teacher_name, ' ', 'course'),
        CHAR_LENGTH(`name`) / 10,
        DATE_ADD(start_date, INTERVAL 5 DAY),
        REVERSE(teacher_name),
        CONCAT('Course ', teacher_name, REVERSE(`description`)),
        DAY(start_date)
    FROM courses 
    WHERE id <= 5
	);


SELECT * FROM courses AS c;
WHERE c.id <= 5

08:23:03	INSERT INTO courses(`name`, duration_hours, start_date,  teacher_name , `description`, university_id )  (     SELECT    CONCAT(teacher_name, ' ', 'course'),         CHAR_LENGTH(`name`) / 10,         DATE_ADD(start_date, INTERVAL 5 DAY),         REVERSE(teacher_name),         CONCAT('Course', teacher_name, REVERSE(`description`))     FROM courses      WHERE id <= 5  )	Error Code: 1136. Column count doesn't match value count at row 1	0.000 sec
