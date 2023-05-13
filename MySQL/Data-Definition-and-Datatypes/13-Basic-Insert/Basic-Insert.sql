CREATE DATABASE soft_uni;
USE soft_uni;

CREATE TABLE towns (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20)
);

INSERT INTO towns (name) VALUES
	('Sofia'),
    ('Plovdiv'),
    ('Varna'),
    ('Burgas');

CREATE TABLE addresses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    address_text VARCHAR(40),
    town_id INT,
    FOREIGN KEY (town_id)
        REFERENCES towns (id)
);
CREATE TABLE departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20)
);

INSERT INTO departments(name) VALUES
	('Engineering'),
    ('Sales'),
    ('Marketing'),
    ('Software Development'),
    ('Quality Assurance');
    
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30),
    middle_name VARCHAR(30),
    last_name VARCHAR(30),
    job_title VARCHAR(20),
    department_id INT,
    hire_date DATE,
    salary DOUBLE(10 , 2 ),
    address_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments (id),
    FOREIGN KEY (address_id)
        REFERENCES addresses (id)
);

INSERT INTO employees (first_name, middle_name, last_name, job_title, department_id, hire_date, salary) VALUES
	('Ivan', 'Ivanov', 'Ivanov','.NET Developer', 4, '2013-02-01',3500.00),
    ('Petar', 'Petrov', 'Petrov','Senior Engineer', 1, '2004-03-02',4000.00),
    ('Maria', 'Petrova', 'Ivanova','Intern', 5, '2016-08-28',525.25),
    ('Georgi', 'Terziev', 'Ivanov','CEO', 2, '2007-12-09',3000.00),
    ('Peter', 'Pan', 'Pan','.Intern', 3, '2016-08-28',599.88);