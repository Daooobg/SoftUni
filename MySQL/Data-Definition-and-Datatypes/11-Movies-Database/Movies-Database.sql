/* • directors (id, director_name, notes)
	o director_name cannot be null
• genres (id, genre_name, notes)
	o genre_name cannot be null
• categories (id, category_name, notes)
	o category_name cannot be null
• movies (id, title, director_id, copyright_year, length, genre_id, category_id, rating, notes)
	o title cannot be null */
    
    CREATE DATABASE movies;
    USE movies;
    
CREATE TABLE directors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    director_name VARCHAR(50) NOT NULL,
    notes TEXT
);

INSERT INTO directors (director_name, notes)
VALUES 
	('Victor', 'NOTES'),
    ('Ivaylo', 'hi'),
    ('Maria',1),
    ('Christine','TEST'),
    ('Maya', 'test');

CREATE TABLE genres (
    id INT PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(20) NOT NULL,
    notes TEXT
);

INSERT INTO genres (genre_name) 
values 
	('test'),
    ('test'),
    ('test'),
    ('test'),
    ('test');

CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(20) NOT NULL,
    notes TEXT
);

INSERT INTO categories (category_name) 
values 
	('test'),
    ('test'),
    ('test'),
    ('test'),
    ('test');

CREATE TABLE movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(20) NOT NULL,
    director_id INT,
    copyright_year YEAR,
    length DOUBLE(10 , 2 ),
    genre_id INT,
    category_id INT,
    rating DOUBLE(2 , 2 ),
    notes TEXT,
    -- this lines need to be removed to pass judge system 
    FOREIGN KEY fk_movies_directors (director_id)
        REFERENCES directors (id),
	FOREIGN KEY fk_movies_genres (genre_id)
		REFERENCES genres (id),
	FOREIGN KEY fk_movies_categories (category_id)
		REFERENCES categories (id)
	-- to here
);

INSERT INTO movies (title, director_id, genre_id, category_id)
VALUES 
	('TEST',1,2,3),
	('test',2,2,2),
    ('TEST',3,4,5),
    ('TEST',5,3,1),
    ('TEST',3,4,2);