import psycopg2

def imprimirBasesDeDatos(connection):
    # Create a cursor
    cursor = connection.cursor()

    # Execute a SQL query to list all tables in the database
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

    # Fetch all the results
    tables = cursor.fetchall()

    # Print the list of table names
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # Close the cursor and connection
    cursor.close()

def imprimirValoresDeTablas(connection):
    # Connect to the database
    cursor = connection.cursor()

    Tablas = ["Stock", "Pedido", "Detalle_Pedido"]

    for tabla in Tablas:

        # Execute the SELECT statement to retrieve all values
        select_query = f"SELECT * FROM {tabla}"
        cursor.execute(select_query)

        # Fetch all rows
        rows = cursor.fetchall()

        print(f"\nTabla {tabla}:")

        # Print the results
        for row in rows:
            print(row)
            
    print ("\n")
    # Close the cursor and the database connection
    cursor.close()
