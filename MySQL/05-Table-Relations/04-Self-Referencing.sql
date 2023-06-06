CREATE TABLE `teachers` (
    `teacher_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50),
    `manager_id` INT
);

ALTER TABLE `teachers` AUTO_INCREMENT = 101;

INSERT INTO `teachers`(`name`) VALUES ('John');

INSERT INTO `teachers`(`name`, `manager_id`) 
	VALUES ('Maya', 106), 
		   ('Silvia', 106), 
           ('Ted', 105), 
           ('Mark', 101), 
           ('Greta', 101);

ALTER TABLE `teachers` 
	ADD CONSTRAINT fk_teachers_teacher_id_manager_id 
		FOREIGN KEY (`manager_id`)
        REFERENCES `teachers`(`teacher_id`);
        