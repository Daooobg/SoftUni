CREATE DATABASE car_rental ;
USE car_rental ;

CREATE TABLE `categories` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `category` VARCHAR(20),
    `daily_rate` DOUBLE(10 , 2 ),
    `weekly_rate` DOUBLE(10 , 2 ),
    `monthly_rate` DOUBLE(10 , 2 ),
    `weekend_rate` DOUBLE(10 , 2 )
);

INSERT INTO `categories` (`category`, `daily_rate`, `weekly_rate`, `monthly_rate`, `weekend_rate`) 
VALUES 
	('SUV', 35.99, 121.99, 302.99, 90.99),
    ('Hatchback', 32.99, 101.99, 282.99, 80.99),
	('Sports car', 62.99, 201.99, 482.99, 150.99);
    

CREATE TABLE `cars` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `plate_number` VARCHAR(8) NOT NULL,
    `make` VARCHAR(20) NOT NULL,
    `model` VARCHAR(20) NOT NULL,
    `car_year` YEAR,
    `category_id` INT,
    `doors` INT,
    `picture` BLOB,
    `car_condition` TEXT,
    `available` BOOLEAN
   --  FOREIGN KEY  fk_car_rental_cars (category_id)
-- 		REFERENCES categories(id)
);

INSERT INTO `cars`(`plate_number`, `make`, `model`, `car_year`, `category_id`, `doors`, `car_condition`, `available`)
VALUES 
	('EW16 SRS', 'Mercedes-Benz', 'Gla Class', 2018, 1, 5, 'brand new', TRUE),
    ('EA16 RRR', 'Mercedes-Benz', 'A Class', 2016, 2, 5, 'brand new', FALSE),
	('VX22 VRF', 'Chevrolet', 'Corvette Z06', 2022, 3, 2, 'brand new', TRUE);


CREATE TABLE `employees` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(20) NOT NULL,
    `last_name` VARCHAR(20) NOT NULL,
    `title` VARCHAR(10) NOT NULL,
    `notes` TEXT
);

INSERT INTO `employees` (`first_name`, `last_name`, `title`, `notes`)
VALUES 
	('George', 'Smith', 'mr', 'text'),
    ('Henry', 'Oliver', 'mr', 'something here'),
    ('Mia', 'William', 'mrs' , 'test');

CREATE TABLE `customers` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `driver_licence_number` VARCHAR(15) NOT NULL,
    `full_name` VARCHAR(30) NOT NULL,
    `address` VARCHAR(50) NOT NULL,
    `city` VARCHAR(20),
    `zip_code` VARCHAR(10),
    `notes` TEXT
);

INSERT INTO `customers` (`driver_licence_number`, `full_name`, `address`, `city`, `zip_code`) 
VALUES 
	('432442IV09DA', 'Ivaylo Ivanov', '401 Canterbury house', 'Dagenham', 'RM8 2GF'),
    ('432DASSV09DA', 'George Ivanov', '6 Campus Avenue', 'Dagenham', 'RM8 2FW'),
    ('432D2341342A', 'Stiven Smith', '24 Barking road', 'Bolton', 'BL3 2MM') ;
  
CREATE TABLE `rental_orders` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `employee_id` INT,
    `customer_id` INT,
    `car_id` INT,
    `car_condition` VARCHAR(20),
    `tank_level` INT(3) NOT NULL,
    `kilometrage_start` INT(30) NOT NULL,
    `kilometrage_end` INT NOT NULL,
    `total_kilometrage` INT NOT NULL,
    `start_date` DATE,
    `end_date` DATE,
    `total_days` INT(10),
    `rate_applied` DOUBLE(10 , 2 ),
    `tax_rate` DOUBLE(10 , 2 ),
    `order_status` VARCHAR(20),
    `notes` TEXT
  --   FOREIGN KEY  fk_car_rental_employees (employee_id)
-- 		REFERENCES employees(id),
-- 	FOREIGN KEY  fk_car_rental_customers (customer_id)
-- 		REFERENCES customers(id),
-- 	FOREIGN KEY  fk_car_rental_cars (car_id)
-- 		REFERENCES cars(id)
);

INSERT INTO `rental_orders` (`employee_id`, `customer_id`, `car_id`, `car_condition`, `tank_level`,
`kilometrage_start`, `kilometrage_end`, `total_kilometrage`, `start_date`, `end_date`,
`total_days`, `rate_applied`, `tax_rate`, `order_status`, `notes`)
VALUES 
	(3,3,3,'GOOD', 10, 100, 420, 320, '2021-10-12', '2021-10-13', 1, 62.99, 20, 'TEST', 'TEST'),
    (2,2,2,'GOOD', 40, 100, 420, 320, '2022-10-12', '2022-10-13', 1, 62.99, 20, 'TEST', 'TEST'),
	(1,2,3,'GOOD', 50, 100, 420, 320, '2022-10-12', '2022-10-13', 1, 62.99, 20, 'TEST', 'TEST');