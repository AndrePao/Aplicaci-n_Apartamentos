import sqlite3

#Clase que contiene el manejo de la base de datos
class Base_datos_conexion:
    #atributos y variables de la base
    def __init__(self):
       pass
               
        
    #metodo que abre la base, duda en declaracion de variables
    def Abrir_conexion(self):
        self.conexion=sqlite3.connect('Tarea_Lenguajes4.db')
        return self.conexion

    #metodo que cierra la conexion con la base de datos
    def Cerrar_conexion(self):
        self.conexion=self.Abrir_conexion()
        print 'conexion cerrada'
        return self.conexion.close()

    #metodo que guarda los cambios en la base
    def commit_conexion(self):
        self.conexion=self.Abrir_conexion()
        return self.conexion.commit()

    def cursor_conexion(self):
        self.conexion=self.Abrir_conexion()
        self.c=self.conexion.cursor()
        return self.c

#Realiza la busqueda de acuerdo a si lo que se pide son apartamentos o dormitorios
    def consultar_Tipo_Alquiler(self,Tipo):
        self.Tipo=Tipo
        self.c=self.cursor_conexion()
        self.Lista_Resultado=[]
        for row in self.c.execute('''SELECT nombre, descripcion, facilidades, caracterisitcas, numero_personas,ubicacion, precio, correo, telefono
        FROM apartamento where tipo_alquiler=? order by precio asc''', (self.Tipo,)):
            self.Lista_Resultado.append(row)
        self.conexion=self.Cerrar_conexion()
        return  self.Lista_Resultado

    #CLASE QUE HEREDE DE CONEXION BASE DE DATOS
    #metodo que inserta la informacion en la tabla apartamento, todavia no sirve
    def Insertar_Informacion(self, id_apartamento, nombre, tipo_alquiler, descripcion, facilidades, ubicacion, precio, correo, telefono, caracteristicas, numero_personas):
        self.id_apartamento=id_apartamento
        self.nombre=nombre
        self.tipo_alquiler=tipo_alquiler
        self.descripcion=descripcion
        self.facilidades=facilidades
        self.ubicacion=ubicacion
        self.precio=precio
        self.correo=correo
        self.telefono=telefono
        self.caracteristicas=caracteristicas
        self.numero_personas=numero_personas
        self.conexion=self.Abrir_conexion()#sqlite3.connect('Tarea_Lenguajes4.db')
        self.c=self.cursor_conexion()
        #self.c= self.conexion.cursor()
        self.c.execute('''INSERT INTO apartamento VALUES (?,?,?,?,?,?,?,?,?,?,?)''',(self.id_apartamento,self.nombre,self.tipo_alquiler,
        self.descripcion,self.facilidades,self.ubicacion,self.precio,self.correo,self.telefono,self.caracteristicas,self.numero_personas))
        #self.conexion=self.Abrir_conexion()
        self.conexion.commit()
        self.conexion.close()#_close=self.Cerrar_conexion()

    #CLASE QUE HEREDE DE CONEXION BASE DE DATOS
    #Realiza la busqueda por precio
"""  def consultar_Precio_Alquiler(self,Precio1,Precio2):
        self.Precio1=Precio1
        self.Precio2=Precio2
        self.c=self.cursor_conexion()
        self.Lista_Resultado=[]
        for row in self.c.execute(SELECT nombre, tipo_alquiler, descripcion, facilidades, caracterisitcas, numero_personas,ubicacion, precio, correo, telefono
        FROM apartamento where precio>? and precio<? order by precio asc, (self.Precio1,self.Precio2,)):
            self.Lista_Resultado.append(row)
        self.conexion=self.Cerrar_conexion()
        return  self.Lista_Resultado"""

    
        
        

