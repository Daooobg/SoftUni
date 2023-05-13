/* id – unique number for every user. There will be no more than 263-1 users. (Auto incremented)
• username – unique identifier of the user will be no more than 30 characters (non Unicode). (Required)
• password – password will be no longer than 26 characters (non Unicode). (Required)
• profile_picture – image with size up to 900 KB.
• last_login_time
• is_deleted – shows if the user deleted his/her profile. Possible states are true or false. */

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(26) NOT NULL,
    profile_picture BLOB,
    last_login_time DATETIME,
    is_deleted BOOLEAN
);

INSERT INTO users(username, password) 
VALUES 
('test', 'test'),
('test', 'test'),
('test', 'test'),
('test', 'test'),
('test', 'test');