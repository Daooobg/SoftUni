CREATE DATABASE table_relations;

CREATE TABLE people (
    person_id INT UNIQUE NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10 , 2 ) DEFAULT 0,
    passport_id INT UNIQUE
);

CREATE TABLE passports (
    passport_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    passport_number VARCHAR(8) UNIQUE
);

ALTER TABLE people
 ADD CONSTRAINT pk_people
	PRIMARY KEY (person_id),
ADD CONSTRAINT fk_people_passports
	FOREIGN KEY (passport_id)
    REFERENCES passports(passport_id);
    

INSERT INTO passports(passport_id, passport_number) 
	VALUES (101, 'N34FG21B'), 
		   (102, 'K65LO4R7'), 
           (103, 'ZE657QP2');

INSERT INTO people(first_name, salary, passport_id) 
	VALUES ('Roberto', 43300.00, 102), 
		   ('Tom', 56100.00, 103), 
           ('Yana', 60200.00, 101);