import psycopg2
# Had to find the right Psycopg2 module 
print('success')

def connect_to_db():
    conn = psycopg2.connect(
    database = "ClientDB",
    host = "localhost",
    user= "dataengineer",
    password = "python",
    port = "5432",)
    
    return conn

     

def get_client_info(table_name,client_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        sql = f" SELECT * FROM assessment.{table_name} WHERE client_id = {client_id};"
        cursor.execute(sql)
        client = cursor.fetchall()
        conn.close()
        return client
    except:
        print('an exception occured')





def update_client_data(table_name,client_id, client_field, data):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        sql = f"UPDATE assessment.{table_name} SET {client_field} = '{data}' WHERE client_id = {client_id};"
        cursor.execute(sql)
        print('table updated')
        conn.commit()
        conn.close()
        client = get_client_info(table_name,client_id)
        return client
    except:
        print('An exception occured')

        


print(get_client_info('client_credentials_ii',120))

print(update_client_data('client_credentials_ii',client_id=100, client_field='clientname', data='Jason Barefeet'))

print(update_client_data('client_credentials_ii',client_id=100, client_field='clientname', data='Jason Barefoot'))