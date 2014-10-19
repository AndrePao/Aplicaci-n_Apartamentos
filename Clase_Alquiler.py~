
#Clase principal en la cual se almacenan los datos principales que comparten el apartamento y la habitacion
class Alquiler:
    
    #se inicializa la clase
    def __init__(self, ID, nombre, tipo_alquiler, ubicacion, precio, correo, telefono, descripcion, num_personas):
       
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
        Base=Base_datos_conexion()
        #metodo que coloca el cursor en la base de datos
        cursor=Base.cursor_conexion()
        #Inserta los datos a la base
        cursor.execute('''INSERT INTO alquiler VALUES (?,?,?,?,?,?,?,?,?)''',(self.ID,self.nombre,self.tipo_alquiler,
        self.descripcion,self.ubicacion,self.precio,self.correo,sefl.telefono,self.numero_personas))
        #Metodo que guarda la informacion en la base de datos
        Base.commit_conexion() 
        

#Clase que hereda de Alquiler a la cual se le agregan las facilidades
class Facilidades (Alquiler):

    #Inicializa la clase de facilidades con todos los parametros correspondientes
    def __init__ (self, ID, nombre, ubicacion, precio, correo, telefono, descripcion, num_personas,
                  nombre,amueblado, cable, agua, luz, internet, num_cuartos, cochera, num_baños)
        Alquiler.__init__(self, ID, nombre, ubicacion, precio, correo, telefono, descripcion, num_personas)
        
    #Asignacion de valores
        self.amueblado= amueblado
        self.cable= cable
        self.agua= agua
        self.luz=luz
        self.internet= internet
        self.num_cuartos= num_cuartos
        self.cochera= cochera
        self.num_baños= num_baños
        
    #Funcion que agrega las facilidades a la base de datos
    def agrega_facilidades (self):

        #Realiza nueva conexion con la base de datos
        Base=Base_datos_conexion()
        #metodo que coloca el cursor en la base de datos
        cursor=Base.cursor_conexion()
        #Inserta los datos a la base
        """cursor.execute('''INSERT INTO facilidades VALUES (?,?,?,?,?,?,?,?)''',(self.amueblado,self.cable,self.agua,
        self.luz,self.internet,self.num_cuartos,self.cochera,sefl.num_baños)) """
        #Metodo que guarda la informacion en la base de datos
        Base.commit_conexion() 

  


#Clase que hereda las facilidades ya que posee todas las caracteristicas de apartamento, sin embargo posee algunas
#adicionales como la comida, servicio de limpieza, servicio de lavanderia y ba;o compartido
class Habitacion (Facilidades):

    def __init__ (self, ID, nombre, ubicacion, precio, correo, telefono, descripcion, num_personas,
                  nombre,amueblado, cable, agua, luz, internet, num_cuartos, cochera, num_baños,
                  comida, servicio_limpieza, servicio_lavanderia, baño_compartido):
      
        Facilidades.__init__ (self, ID, nombre, ubicacion, precio, correo, telefono, descripcion, num_personas,
                  nombre,amueblado, cable, agua, luz, internet, num_cuartos, cochera, num_baños)
        
        self.comida= comida
        self.servicio_limpieza= servicio_limpieza
        self.servicio_lavanderia= servicio_lavanderia
        self.baño_compartido= baño_compartido














    
    
        
    
