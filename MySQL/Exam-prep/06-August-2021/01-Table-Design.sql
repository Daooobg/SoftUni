CREATE DATABASE exam_06_Aug_2021;
USE exam_06_Aug_2021;

CREATE TABLE addresses (
	id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL
);

CREATE TABLE categories (
	id INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(10) NOT NULL
);

CREATE TABLE offices (
	id INT PRIMARY KEY AUTO_INCREMENT,
    workspace_capacity INT NOT NULL,
    website VARCHAR(50),
    address_id INT NOT NULL,
    CONSTRAINT fk__offices_address_id__addresses_id
		FOREIGN KEY (address_id)
        REFERENCES addresses(id)
);

CREATE TABLE employees (
	id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    job_title VARCHAR(20) NOT NULL,
    happiness_level CHAR(1) NOT NULL
);

CREATE TABLE teams  (
	id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(40) NOT NULL,
    office_id INT NOT NULL,
    leader_id INT UNIQUE NOT NULL,
    CONSTRAINT fk__teams_office_id__offices_id
		FOREIGN KEY (office_id)
        REFERENCES offices(id),
	CONSTRAINT fk__teams_leader_id__employees_id
		FOREIGN KEY (leader_id)
        REFERENCES employees(id)
);

CREATE TABLE games (
	id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) UNIQUE NOT NULL,
    `description` TEXT,
    rating FLOAT NOT NULL DEFAULT 5.5,
    budget DECIMAL(10, 2) NOT NULL,
    release_date DATE,
    team_id INT NOT NULL,
    CONSTRAINT fk__games_team_id__teams_id
		FOREIGN KEY (team_id)
        REFERENCES teams(id)
);

CREATE TABLE games_categories (
	game_id INT NOT NULL,
    category_id INT NOT NULL,
    CONSTRAINT pk_games_categories PRIMARY KEY (game_id, category_id)
);