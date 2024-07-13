import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="tu_contraseña",  # Cambia esto por tu contraseña
            database="new_base"
        )
        if connection.is_connected():
            print("Conexión a MySQL DB exitosa")
    except Error as e:
        print(f"El error '{e}' ocurrió")
    
    return connection

def agregar_empleado(connection, nombre, puesto, salario):
    cursor = connection.cursor()
    query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
    values = (nombre, puesto, salario)
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Empleado agregado exitosamente")
    except Error as e:
        print(f"El error '{e}' ocurrió")

def consultar_empleados(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM empleados"
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Error as e:
        print(f"El error '{e}' ocurrió")

def actualizar_empleado(connection, empleado_id, nombre, puesto, salario):
    cursor = connection.cursor()
    query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
    values = (nombre, puesto, salario, empleado_id)
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Empleado actualizado exitosamente")
    except Error as e:
        print(f"El error '{e}' ocurrió")

def eliminar_empleado(connection, empleado_id):
    cursor = connection.cursor()
    query = "DELETE FROM empleados WHERE id = %s"
    try:
        cursor.execute(query, (empleado_id,))
        connection.commit()
        print("Empleado eliminado exitosamente")
    except Error as e:
        print(f"El error '{e}' ocurrió")

def menu():
    connection = create_connection()

    while True:
        print("\nMenu:")
        print("1. Agregar Empleado")
        print("2. Consultar Empleados")
        print("3. Actualizar Empleado")
        print("4. Eliminar Empleado")
        print("5. Salir")
        
        choice = input("Elige una opción: ")

        if choice == '1':
            nombre = input("Nombre: ")
            puesto = input("Puesto: ")
            salario = float(input("Salario: "))
            agregar_empleado(connection, nombre, puesto, salario)
        elif choice == '2':
            consultar_empleados(connection)
        elif choice == '3':
            empleado_id = int(input("ID del Empleado: "))
            nombre = input("Nuevo Nombre: ")
            puesto = input("Nuevo Puesto: ")
            salario = float(input("Nuevo Salario: "))
            actualizar_empleado(connection, empleado_id, nombre, puesto, salario)
        elif choice == '4':
            empleado_id = int(input("ID del Empleado: "))
            eliminar_empleado(connection, empleado_id)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
