CREATE DATABASE exam_10_April_2022;
USE exam_10_April_2022;

CREATE TABLE countries (
	id INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL UNIQUE,
    continent VARCHAR(30) NOT NULL,
    currency VARCHAR(5) NOT NULL
);

CREATE TABLE genres (
	id INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE actors (
	id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birthdate DATE NOT NULL,
    height INT,
    awards INT,
    country_id INT NOT NULL,
    CONSTRAINT fk__actors_country_id__countries_id
		FOREIGN KEY (country_id)
        REFERENCES countries(id)
);

CREATE TABLE movies_additional_info(
	id INT PRIMARY KEY AUTO_INCREMENT,
    rating DECIMAL(10, 2) NOT NULL,
    runtime INT NOT NULL,
    picture_url VARCHAR(80) NOT NULL,
    budget DECIMAL(10, 2),
    release_date DATE NOT NULL,
    has_subtitles TINYINT(1),
    `description` TEXT
);

CREATE TABLE movies (
	id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(70) NOT NULL UNIQUE,
    country_id INT NOT NULL,
    movie_info_id INT NOT NULL UNIQUE,
    CONSTRAINT fk__movies_country_id__countries_id
		FOREIGN KEY (country_id)
        REFERENCES countries(id),
	CONSTRAINT fk__movies_movie_info_id__movies_additional_info_id
		FOREIGN KEY (movie_info_id)
        REFERENCES movies_additional_info(id)
);

CREATE TABLE movies_actors (
	movie_id INT,
    actor_id INT,
    CONSTRAINT fk__movies_actors_movie_id__movies_id
		FOREIGN KEY (movie_id)
        REFERENCES movies(id),
	CONSTRAINT fk__movies_actors_actor_id__actors_id
		FOREIGN KEY (actor_id)
        REFERENCES actors(id)
);

CREATE TABLE genres_movies (
	genre_id INT,
    movie_id INT
);

ALTER TABLE genres_movies
	ADD CONSTRAINT fk__genres_movies_movie_id__movies_id
		FOREIGN KEY (movie_id)
        REFERENCES movies(id),
	ADD CONSTRAINT fk__genres_movies_genre_id__genres_id
		FOREIGN KEY (genre_id)
        REFERENCES genres(id);