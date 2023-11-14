import psycopg2
import random

def drop(connection):

    Tablas = ["Detalle_Pedido", "Stock", "Pedido"]

    # Create a cursor
    cursor = connection.cursor()

    try:
        for tabla in Tablas:
            delete_query = f"DROP TABLE {tabla}"
            cursor.execute(delete_query)
        print("La base de datos ha sido borrada")
    except:
        print("La base de datos no existía previamente")
    
    connection.commit()

    # Close the cursor and connection
    cursor.close()

def eliminarDetallesPedido(cursor, Cpedido):

    # Execute a SQL query

    cursor.execute(f"SELECT Cproducto FROM Detalle_Pedido WHERE Cpedido = %s", (Cpedido,))
    productos = cursor.fetchall()

    tabla_a_modificar = 'Stock'
    table_name = 'Detalle_Pedido'

    for producto in productos:

        select_query = f"SELECT Cantidad FROM {table_name} WHERE Cpedido = %s AND Cproducto = %s"
        cursor.execute(select_query, (Cpedido, producto))
        
        cantidad_en_detalle_pedido = cursor.fetchone()[0] 

        delete_query = f"DELETE FROM {table_name} WHERE Cpedido = %s AND Cproducto = %s"
        cursor.execute(delete_query, (Cpedido, producto))
        update_query = f"UPDATE {tabla_a_modificar} SET Cantidad = Cantidad + %s WHERE Cproducto = %s"
        cursor.execute(update_query, (cantidad_en_detalle_pedido, producto))
