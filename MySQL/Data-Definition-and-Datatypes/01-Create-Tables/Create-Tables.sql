create database minions;
use minions;

--  minions (id, name, age)
-- towns (town_id,name) 

CREATE TABLE minions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(47),
    age INT
);


CREATE TABLE towns (
    town_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(47),
    age INT
);
