CREATE TABLE `students` (
    `student_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL
);

CREATE TABLE `exams` (
    `exam_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL
);

ALTER TABLE `exams` AUTO_INCREMENT = 101;

CREATE TABLE `students_exams` (
    `student_id` INT NOT NULL,
    `exam_id` INT NOT NULL,
    CONSTRAINT pk_students_exam
		PRIMARY KEY (`student_id`, `exam_id`),
    CONSTRAINT fk_students_exams_student_id_students_id FOREIGN KEY (`student_id`)
        REFERENCES `students` (`student_id`),
    CONSTRAINT fk_students_exams_exam_id_exams_exam_id FOREIGN KEY (`exam_id`)
        REFERENCES `exams` (`exam_id`)
);

INSERT INTO `students`(`name`)
	VALUES ('Mila'), ('Toni'), ('Ron');
    
INSERT INTO `exams`(`name`) 
	VALUES('Spring MVC'), ('Neo4j'), ('Oracle 11g');
    
INSERT INTO `students_exams` (`student_id`, `exam_id`) 
	VALUES (1, 101), (1, 102), (2, 101), (3, 103), (2, 102), (2, 103); 