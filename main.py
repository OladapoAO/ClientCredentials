import psycopg2
# Had to find the right Psycopg2 module 
print('success')

def connect_to_db():
    try:
     conn = psycopg2.connect(
     database = "ClientDB",
     host = "localhost",
     user= "dataengineer",
     password = "python",
     port = "5432",)
     return conn
    except psycopg2.OperationalError as e:
        print(e)

     

def get_client_info(table_name,client_id):
    if type(client_id) != int:
        raise TypeError('Please enter an integer as the client id')
    else:
         conn = connect_to_db()
         cursor = conn.cursor()
         sql = f" SELECT * FROM assessment.{table_name} WHERE client_id = {client_id};"
         cursor.execute(sql)
         client = cursor.fetchall()
         conn.close()
         return client





def update_client_data(table_name,client_id, table_column, data):
    if type(client_id) != int:
        raise TypeError('Please enter an integer as the client id')
    else:
        conn = connect_to_db()
        cursor = conn.cursor()
        sql = f"UPDATE assessment.{table_name} SET {table_column} = '{data}' WHERE client_id = {client_id};"
        cursor.execute(sql)
        print('table updated')
        conn.commit()
        conn.close()
        client = get_client_info(table_name,client_id)
        return client
        


print(get_client_info('client_credentials_ii',1000))

print(update_client_data('client_credentials_ii',client_id=100, table_column='clientname', data='Jason Barefeet'))

print(update_client_data('client_credentials_ii',client_id=100, table_column='clientname', data='Jason Barefoot'))