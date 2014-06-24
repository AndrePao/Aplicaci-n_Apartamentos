import Clase_Base_datos
#Clase principal en la cual se almacenan los datos principales que comparten el apartamento y la habitacion
class Alquiler:

    #se inicializa la clase
    def __init__(self,ID, nombre, tipo_alquiler, ubicacion, precio, correo, telefono, descripcion, num_personas):

                #Asignacion de valores 
        self.ID= ID
        self.nombre= nombre
        self.tipo_alquiler= tipo_alquiler
        self.descripcion= descripcion
        self.ubicacion= ubicacion
        self.precio= precio
        self.correo= correo
        self.telefono= telefono
        self.num_personas= num_personas


#Funcion que agrega el alquiler a la base de datos
    def agrega_alquiler(self):

        #Realiza nueva conexion con la base de datos
        Base=Clase_Base_datos.Base_datos_conexion()
        #metodo que coloca el cursor en la base de datos
        cursor=Base.cursor_conexion()
        #Inserta los datos a la base
        cursor.execute('''INSERT INTO alquiler VALUES (?,?,?,?,?,?,?,?,?)''',(self.ID,self.nombre,self.tipo_alquiler,
        self.descripcion,self.ubicacion,self.precio,self.correo, self.telefono, self.num_personas))
        #Metodo que guarda la informacion en la base de datos
        Base.commit_conexion() 


#Clase que hereda de Alquiler a la cual se le agregan las facilidades
class Facilidades (Alquiler):

#Inicializa la clase de facilidades con todos los parametros correspondientes
    def __init__ (self, ID, nombre, tipo_alquiler, ubicacion, precio, correo, telefono, descripcion, num_personas,
          amueblado, cable, agua, luz, internet, num_cuartos, cochera, num_banos, bano_compartido, comida, servicio_limpieza,servicio_lavanderia):
        Alquiler.__init__(self,ID, nombre, tipo_alquiler, ubicacion, precio, correo, telefono, descripcion, num_personas)

#Asignacion de valores
        self.amueblado= amueblado
        self.cable= cable
        self.agua= agua
        self.luz=luz
        self.internet= internet
        self.num_cuartos= num_cuartos
        self.cochera= cochera
        self.num_banos= num_banos
        self.comida= comida
        self.servicio_limpieza= servicio_limpieza
        self.servicio_lavanderia= servicio_lavanderia
        self.bano_compartido= bano_compartido

#Funcion que agrega las facilidades a la base de datos
    def agrega_facilidades (self):

        #Realiza nueva conexion con la base de datos
        Base=Clase_Base_datos.Base_datos_conexion()
        #metodo que coloca el cursor en la base de datos
        cursor=Base.cursor_conexion()
        #Inserta los datos a la base
        cursor.execute('''INSERT INTO facilidades VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',(self.ID, self.num_cuartos, self.num_banos, self.bano_compartido, self.servicio_limpieza, self.amueblado, self.comida, self.servicio_lavanderia, self.cochera, self.agua, self.luz, self.cable, self.internet))
        #Metodo que guarda la informacion en la base de datos
        Base.commit_conexion()  

 
def numero_filas():
	Base=Clase_Base_datos.Base_datos_conexion()
	cursor=Base.cursor_conexion()
        c=1
        for e in cursor.execute('''SELECT id_apartamento from alquiler'''):
            c+=1
	print c
        return c
numero_filas()

