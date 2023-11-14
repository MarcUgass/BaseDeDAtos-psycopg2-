import psycopg2
from Include.GeneradorBaseDeDatos import crearBaseDeDatos
from Include.BorrarTablas import drop, eliminarDetallesPedido
from Include.ComprobarBasesDeDatos import imprimirValoresDeTablas
from Include.AñadirValores import stock, insertarPedido, insertarDetallePedido

connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
connection.autocommit = False
while True:
    print("1. Borrado y nueva creacion de las tablas e insercion de las tuplas en Stock")
    print("2. Dar de alta nuevo pedido")
    print("3. Mostrar contenido de las tablas de la base de datos")
    print("4. Salir del programa y cerrar conexión a base de datos")
    opcion = input("Ingrese una opcion: ")

    
    if opcion == "1":
        drop(connection)
        crearBaseDeDatos(connection)
        stock(connection)
        print("\nTablas creadas e insertadas")
        print("\n\n")

    elif opcion == "2":
        print ("Insertar código de pedido: ")
        codPedido = input()
        print ("Insertar código de cliente (DNI): ")
        codCliente = input()
        print ("Insertar fecha de pedido (YYYY-MM-DD): ")
        fechaPedido = input()

        cursor = connection.cursor()
        insertarPedido(cursor, codPedido, codCliente, fechaPedido)
        print ("Pedido insertado\n")

        while True:
            print("1. Añadir detalle de producto")
            print("2. Eliminar todos los detalles de producto")
            print("3. Cancelar pedido")
            print("4. Finalizar pedido")
            opcion = input("Ingrese una opcion: ")

            if opcion == "1":
                print ("Insertar código de producto:")
                codProducto = input()
                print ("Insertar cantidad: ")
                cantidad = input()
                insertarDetallePedido(cursor, codPedido, codProducto, cantidad)
                imprimirValoresDeTablas(connection)

            elif opcion == "2":
                eliminarDetallesPedido(cursor, codPedido)
                print ("Detalles eliminados\n")
                imprimirValoresDeTablas(connection)

            elif opcion == "3":
                connection.rollback()
                print ("\nPedido eliminado\n")
                imprimirValoresDeTablas(connection)
                break

            elif opcion == "4":
                connection.commit()
                print ("Pedido finalizado\n")
                break
            else:
                print("Opcion invalida")

        print("\n\n")

    elif opcion == "3":
       imprimirValoresDeTablas(connection)
       print("\n\n")

    elif opcion == "4":
        connection.close()
        print ("Conexion cerrada\n")
        quit()

    else:
        print("Opcion invalida")