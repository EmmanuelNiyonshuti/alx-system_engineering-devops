--create holberton user and grant them permissions

--CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
--GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';


--create database and a table in it
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50));
INSERT INTO nexus6 (name) VALUES("Leon");
