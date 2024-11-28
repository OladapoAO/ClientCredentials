CREATE DATABASE ClientDB;

CREATE SCHEMA assessment;

CREATE TABLE assessment.Client_Credentials (
    client_id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name  TEXT,
    email TEXT,
    password VARCHAR(16) NOT NULL,
    created_date TIMESTAMP NOT NULL
);

CREATE TABLE assessment.Client_Credentials_II (
    client_id SERIAL PRIMARY KEY,
    ClientName TEXT NOT NULL,
    email TEXT,
    password VARCHAR(16) NOT NULL,
    created_date TIMESTAMP NOT NULL
);