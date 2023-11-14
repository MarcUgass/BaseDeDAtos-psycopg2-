import psycopg2
import random
from datetime import datetime, timedelta

def fecha():
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2023, 1, 1)

    # Calculate the number of days between the start and end dates
    delta = end_date - start_date

    # Generate a random number of days between 0 and the total number of days in the range
    random_days = random.randint(0, delta.days)

    # Create a random date by adding the random number of days to the start date
    random_date = start_date + timedelta(days=random_days)

    return random_date

def stock(connection):
    
    random.seed(1234)

    numEntradas = 10

    tablaValores = range(1,numEntradas + 1)

    # Create a cursor
    cursor = connection.cursor()

    # Execute a SQL query

    table_name = 'Stock'
    insert_query = f"INSERT INTO {table_name} (Cproducto, Cantidad) VALUES (%s, %s)"

    for i in tablaValores:

        cantidad = random.randint(0,500) * 10

        cursor.execute(insert_query, (i, cantidad))
    """
    table_name = 'Pedido'
    insert_query = f"INSERT INTO {table_name} (Cpedido, Ccliente, Fecha_pedido) VALUES (%s, %s, %s)"

    for i in tablaValores:

        codCliente = random.randint(0,1000)

        cursor.execute(insert_query, (i, codCliente, fecha()))

    table_name = 'Detalle_Pedido'

    insert_query = f"INSERT INTO {table_name} (Cproducto, Cpedido, Cantidad) VALUES (%s, %s, %s)"
    for i in tablaValores:

        # Execute the INSERT statement
        # Replace 'column_name' with the name of the column where you want to insert the value

        valores = random.sample(tablaValores,random.randint(1,6))
        
        for j in valores:
            cantidad = random.randint(0,500)
            cursor.execute(insert_query, (i, j, cantidad))
    """


    # Close the cursor and connection
    connection.commit()
    cursor.close()

def insertarPedido(cursor, Cpedido, Ccliente, Fecha_pedido):

    # Execute a SQL query

    table_name = 'Pedido'
    insert_query = f"INSERT INTO {table_name} (Cpedido, Ccliente, Fecha_pedido) VALUES (%s, %s, %s)"

    cursor.execute(insert_query, (Cpedido, Ccliente, Fecha_pedido))


def insertarDetallePedido(cursor, Cpedido, Cproducto, Cantidad):
    
    # Execute a SQL query

    tabla_a_comprobar = 'Stock'

    cursor.execute(f"SELECT Cantidad FROM {tabla_a_comprobar} WHERE Cproducto = %s", (Cproducto,))
    
    table_name = 'Detalle_Pedido'

    cantidad_en_stock = cursor.fetchone()

    if cantidad_en_stock == None:
        print(f"Error: No existe el producto {Cproducto}")
        return 1
    else:
        cantidad_en_stock = cantidad_en_stock[0]

        if cantidad_en_stock < int(Cantidad):
            print(f"Error: No hay suficiente stock del producto {Cproducto}")
            return 1
        else:
            update_query = f"UPDATE {tabla_a_comprobar} SET Cantidad = Cantidad - %s WHERE Cproducto = %s"
            cursor.execute(update_query, (Cantidad, Cproducto))
            insert_query = f"INSERT INTO {table_name} (Cpedido, Cproducto, Cantidad) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (Cpedido, Cproducto, Cantidad))
