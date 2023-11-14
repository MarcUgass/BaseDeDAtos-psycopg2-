import psycopg2
def crearBaseDeDatos(connection):

    # Create a cursor
    cursor = connection.cursor()

    # Execute a SQL query



    cursor.execute("""CREATE TABLE Stock (
        Cproducto INT PRIMARY KEY,
        Cantidad INT
    );""")

    cursor.execute("""CREATE TABLE Pedido (
        Cpedido INT PRIMARY KEY,
        Ccliente INT,
        Fecha_pedido DATE
    );""")

    cursor.execute("""CREATE TABLE Detalle_Pedido(
        Cproducto INT REFERENCES Stock (Cproducto),
        Cpedido INT REFERENCES Pedido (Cpedido),
        Cantidad INT CHECK (Cantidad > 0),
        PRIMARY KEY (Cproducto, Cpedido)
    );""")
    connection.commit()

    # Close the cursor and connection
    cursor.close()