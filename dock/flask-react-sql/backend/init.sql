CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE IF NOT EXISTS users (
                                     id INT AUTO_INCREMENT PRIMARY KEY,
                                     name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
    );

INSERT INTO users (name, email) VALUES
                                    ('John Doe', 'john@example.com'),
                                    ('Jane Smith', 'jane@example.com');

SELECT 'init.sql executed successfully' AS status;
