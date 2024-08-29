import mysql.connector
from mysql.connector import Error

class Conexion:
    def conectar():
            
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="biblio"
                )
                print("Se conectó correctamente")
                return mydb
            except Error as e:
                print(f"Pequeño Error en la conexión", str(e))

    def desconectar(self, mydb):
        mydb.close()

class Biblioteca(Conexion): 
    

    def prestar(self):
        pass           

    def devolver(self):
        pass

    def listardisponibles(self):
        pass

    def listarprestados(self):
        pass

class Libro(Conexion):
    def __init_(self, isbn, titulo, autor, disponibilidad):
        self.isbn = isbn
        self.titulo =  titulo
        self.autor = autor
        self.disponibilidad = disponibilidad

    def insertar(self, isbn, titulo, autor, disponibilidad):
        sql="INSERT INTO libro (isbn, titulo, autor, disponibilidad) VALUES (%s, %s, %s, %s)"
        val = (isbn, titulo, autor, disponibilidad)
        try:
            mydb = Conexion.conectar()
            myCursor = mydb.cursor()
            myCursor.execute(sql,val)
            mydb.commit()
            print(f"Inserción exitosa")
        except Error as e:
            print(f"Pequeño Error en la consulta", str(e))
    
    def buscar(self):
        pass
    
    def actualizar(self):
        pass

    def eliminar(self):
        pass

class biblio(Biblioteca,Libro):
    pass

myApp = biblio()
myApp.insertar("1237355355","Cien años de soledad","Gabriel García Márquez","1")