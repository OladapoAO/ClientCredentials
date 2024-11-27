CREATE DATABASE ClientDB;

CREATE SCHEMA assessment;

CREATE TABLE assessment.Client_Credentials (
    client_id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name  TEXT,
    email TEXT,
    password CHAR(256) NOT NULL,
    created_date TIMESTAMP NOT NULL
);