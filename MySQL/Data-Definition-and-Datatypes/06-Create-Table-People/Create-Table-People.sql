-- id – unique number for every person there will be no more than 231-1people. (Auto incremented)
-- • name – full name of the person will be no more than 200 Unicode characters. (Not null)
-- • picture – image with size up to 2 MB. (Allow nulls)
-- • height – In meters. Real number precise up to 2 digits after floating point. (Allow nulls)
-- • weight – In kilograms. Real number precise up to 2 digits after floating point. (Allow nulls)
-- • gender – Possible states are m or f. (Not null)
-- • birthdate – (Not null)
-- • biography – detailed biography of the person it can contain max allowed Unicode characters. (Allow nulls)

CREATE TABLE people (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    picture BLOB,
    height DOUBLE(10 , 2 ),
    weight DOUBLE(10 , 2 ),
    gender CHAR(1) NOT NULL,
    birthdate DATE NOT NULL,
    biography TEXT
);

INSERT INTO people(name, gender, birthdate)
VALUES 
('Ivan', 'm', DATE(NOW())),
('George', 'm', DATE(NOW())),
('Maria', 'f', DATE(NOW())),
('Victor', 'm', DATE(NOW())),
('Christine', 'm', DATE(NOW()));