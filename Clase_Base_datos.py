import sqlite3

#Clase que contiene el manejo de la base de datos
class Base_datos_conexion:
    conexion=sqlite3.connect('Tarea_Lenguajes4.db')#Variable que abre la base de datos
    def __init__(self):
       pass
    #metodo que cierra la conexion con la base de datos
    def Cerrar_conexion(self):
        return self.conexion.close()

    #metodo que guarda los cambios en la base
    def commit_conexion(self):
        return self.conexion.commit()
    
    #metodo que maneja el cursor de la base de datos
    def cursor_conexion(self):
        self.c=self.conexion.cursor()
        return self.c
#fin de la clase
    
#Realiza la busqueda de acuerdo a si lo que se pide son apartamentos o dormitorios
def consultar_Tipo_Alquiler(Tipo):
    Base=Base_datos_conexion()
    cursor=Base.cursor_conexion()
    Lista_Resultado=[]
    for row in cursor.execute('''SELECT nombre, descripcion, numero_personas,ubicacion, precio, correo, telefono
    FROM alquiler where tipo_alquiler=? order by precio asc''', (Tipo,)):
        Lista_Resultado.append(row)
    
    return  Lista_Resultado

def Insertar_Informacion(id_apartamento, nombre, tipo_alquiler, descripcion, ubicacion, precio, correo, telefono, numero_personas):
    Base=Base_datos_conexion()
    cursor=Base.cursor_conexion() #metodo que coloca el cursor en la base de datos
    cursor.execute('''INSERT INTO alquiler VALUES (?,?,?,?,?,?,?,?,?)''',(id_apartamento,nombre,tipo_alquiler,
    descripcion,ubicacion,precio,correo,telefono,numero_personas))
    Base.commit_conexion() #metodo que guarda la informacion en la base de datos
   
