COPY assessment.Client_Credentials (client_id, first_name, last_name, email, password, created_date) 
FROM '/Users/dapoaowolabi/Downloads/Client_Data.csv'
DELIMITER ','
CSV HEADER
QUOTE '\"' 
ESCAPE '\"';

COPY assessment.Client_Credentials_II (client_id, clientname, email, password, created_date) 
FROM '/Users/dapoaowolabi/Downloads/Client_Data_II.csv'
DELIMITER ','
CSV HEADER
QUOTE '\"' 
ESCAPE '\"';
