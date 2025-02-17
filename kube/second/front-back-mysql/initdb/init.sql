CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

CREATE TABLE IF NOT EXISTS items (
                                     id INT PRIMARY KEY AUTO_INCREMENT,
                                     name VARCHAR(100) NOT NULL
    );
