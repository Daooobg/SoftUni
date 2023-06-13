CREATE TABLE countries (
	id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(40) NOT NULL UNIQUE,
    population INT,
    country_id INT NOT NULL,
    CONSTRAINT fk__cities_country_id__countries_id
		FOREIGN KEY (country_id)
        REFERENCES countries(id)
);

CREATE TABLE universities (
	id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(60) NOT NULL UNIQUE,
    address VARCHAR(80) NOT NULL UNIQUE,
    tuition_fee DECIMAL(19, 2) NOT NULL,
    number_of_staff INT,
    city_id  INT,
    CONSTRAINT fk__universities_city_id__cities_id
		FOREIGN KEY (city_id)
        REFERENCES cities(id)
);

CREATE TABLE students (
	id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    age INT,
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    is_graduated TINYINT(1) NOT NULL,
    city_id INT,
    CONSTRAINT fk__students_city_id__cities_id
		FOREIGN KEY (city_id)
        REFERENCES cities(id)
);

CREATE TABLE courses (
	id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(40) NOT NULL UNIQUE,
    duration_hours DECIMAL(19, 2),
    start_date DATE,
    teacher_name VARCHAR(60) NOT NULL UNIQUE,
    `description` TEXT,
    university_id INT,
    CONSTRAINT fk__courses_university_id__universities_id
		FOREIGN KEY (university_id)
        REFERENCES universities(id)
);

CREATE TABLE students_courses (
	grade DECIMAL(19, 2) NOT NULL,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    CONSTRAINT fk__students_courses_student_id__students_id
		FOREIGN KEY (student_id)
        REFERENCES students(id),
    CONSTRAINT fk__students_courses_course_id__courses_id
		FOREIGN KEY (course_id)
        REFERENCES courses(id)
);