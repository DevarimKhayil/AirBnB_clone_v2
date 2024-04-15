-- setup_mysql_dev.sql
-- Script to configure the MySQL database for the Airbnb clone project

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Drop the user if it exists to reset privileges
DROP USER IF EXISTS 'hbnb_dev'@'localhost';

-- Create the user with the specified password if it does not exist
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the development database to the development user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Ensure the user has SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the changes made by the GRANT statement
FLUSH PRIVILEGES;

