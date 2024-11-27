CREATE USER dataengineer WITH PASSWORD 'python';

GRANT USAGE ON SCHEMA assessment TO dataengineer;

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA assessment TO dataengineer;


