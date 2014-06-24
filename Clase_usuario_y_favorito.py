import Clase_Base_datos
#clase usuario, agrega el usuario a la base de datos
class Usuario():

    def __init__(self, correo):
        self.correo=correo
        self.c=Clase_Base_datos.Base_datos_conexion()
        self.cursor=self.c.cursor_conexion()
    #metodo que agrega un nuevo usuario  a la base de datos
    def Insertar_usuario(self):
        self.cursor.execute('''INSERT INTO usuario (correo) VALUES (?)''', (self.correo,))
        self.c.commit_conexion()
    #metodo que verifica si el usuario se encuentra registrado en la base de datos, es el metodo q se invoca desde flask
    def verificar_usuario(self):
        variable=""
        for e in self.cursor.execute('''SELECT correo from usuario where correo=?''', (self.correo,)):
            variable=e
        if variable=="":
            self.Insertar_usuario()
        
#clase que agrega y consulta los apartamentos favoritos de un usuario 
class Favorito(Usuario):
    def __init__(self,correo):
        Usuario.__init__(self,correo)

    #guarda los apartamentos y habitaciones favoritos de un usuario
    def agregar_favorito(self,correo, id_alquiler):
        self.alquiler=id_alquiler
        self.cursor.execute('''INSERT INTO favoritos VALUES (?,?)''', (self.alquiler,self.correo,))
        self.c.commit_conexion()

    #consulta los apartamentos y habitaciones de un usuario
    def consultar_favorito(self):
        self.listaF=[]
        
        for e in self.cursor.execute('''SELECT a.nombre, a.tipo_alquiler,a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono,
        f.n_dormitorio, f.n_bano, f.amueblado, f.cochera, f.agua, f.luz, f.cable, f.internet,f.limpieza, f.lavanderia, f.comida
        from alquiler a, facilidades f, favoritos fa where fa.correo=? and
        fa.id_apartamento=a.id_apartamento and a.id_apartamento=f.id_apartamento order by precio asc''', (self.correo,)):
             self.listaF+=[e]
        return self.listaF
