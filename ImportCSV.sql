COPY assessment.Client_Credentials (client_id, first_name, last_name, email, password, created_date) 
FROM '/Users/dapoaowolabi/Downloads/Client_Data.csv'
DELIMITER ','
CSV HEADER
QUOTE '\"' 
ESCAPE '\"';


