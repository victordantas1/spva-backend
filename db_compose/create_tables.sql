CREATE DATABASE IF NOT EXISTS spva;

use spva;

CREATE TABLE IF NOT EXISTS role_user (
    role_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS user_app (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    birthdate DATE,
    email VARCHAR(255) NOT NULL UNIQUE,
    resume_path VARCHAR(255),
    role_id INT NOT NULL,
    FOREIGN KEY (role_id) references role_user(role_id)
);

CREATE TABLE IF NOT EXISTS phone_number (
    phone_number_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    number VARCHAR(20) NOT NULL UNIQUE,
    FOREIGN KEY (user_id) references user_app(user_id)
);

CREATE TABLE IF NOT EXISTS job (
    job_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    position VARCHAR(255) NOT NULL,
    category ENUM('remote', 'on-site', 'hybrid') NOT NULL,
    create_date DATE,
    responsibilities TEXT,
    requirements TEXT,
    level VARCHAR(50),
    contract_type VARCHAR(50),
    schedule VARCHAR(100),
    salary_range VARCHAR(100),
    company VARCHAR(255),
    FOREIGN KEY (user_id) references user_app(user_id)
);

CREATE TABLE IF NOT EXISTS user_job (
    user_id INT NOT NULL,
    job_id INT NOT NULL,
    application_date DATE NOT NULL,
    status ENUM('sent', 'analyse', 'rejected', 'accepted') NOT NULL DEFAULT 'sent',
    resume_path VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id, job_id),
    FOREIGN KEY (user_id) REFERENCES user_app(user_id),
    FOREIGN KEY (job_id) REFERENCES job(job_id)
);