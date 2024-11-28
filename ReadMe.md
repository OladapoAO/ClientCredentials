Issues Encountered
1. I had to find the right Psyscopg2 module for My computer, I was using a mac so i did some research and found I needed to install the Psycopg2-Binary module.
2. On my first initial analysis of the CSV Data, I noticed that we had some data quality issues. there were was an extra column for all rows in the data.
Client with ID 34 had the wrong data and datatype in the created_on column and Client with ID "Goly" is not the correct datatype for the primary key.
In order to fix this issues I used pandas to clean my data by removing the extra columns and replacing the incorrect values with the correct datatype and value. Please refer to the "CSV Cleanup.ipynb" file for reference.
3. When it was time to load the data, i had to factor in how PostgreSQL would evaulate quotes '"' in the csv file.
4. I also created two tables one that has the clients first name & last name in separate columns, the other has the two combined into one column called clientname i was able to manipulate the csv file with pandas and concatenate the two columns together into one.

Setting Up My Environment
- Install PostgreSQL.
- Setup the database, schema & sql users with the default superuser "postgres".
- Check the properties feature of your database to grab relevant information like "Host", "Port".
- Create a Python Virtual Environment.
- Install Psycopg2-binary & Pandas.
- Create a connection to the database using Python & Psycopg2.
- Build your python functions