import psycopg2
import random

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

Tablas = ["Detalle_Pedido", "Stock", "Pedido"]

connection.autocommit = False

# Create a cursor
cursor = connection.cursor()


for tabla in Tablas:
    delete_query = f"DELETE FROM {tabla}"
    cursor.execute(delete_query)

connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
