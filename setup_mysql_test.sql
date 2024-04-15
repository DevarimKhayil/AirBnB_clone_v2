-- setup_mysql_test.sql
-- Script to configure the MySQL database for Airbnb clone project - Testing Environment

-- Create the test database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it does not exist, else do nothing to avoid errors
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant the test user full privileges on the test database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Ensure the test user has SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the changes made by the GRANT statement
FLUSH PRIVILEGES;

