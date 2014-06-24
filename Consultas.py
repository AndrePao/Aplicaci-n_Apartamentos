import Clase_Base_datos
class conversiones:
    def __init__(self):
        pass       

    def convertir_minuscula(self,texto):
        self.texto=texto
        return self.texto.lower()

    def convertir_entero(self,numero):
        self.numero=numero
        return int(self.numero)

#quien valida si no se encontraron resultados con la busqueda
#clase que  busca informacion tanto de apartamentos como de habitaciones..
class consultas_general:
    
    def __init__(self):
        self.c=Clase_Base_datos.Base_datos_conexion()
        self.cursor=self.c.cursor_conexion()
        self.validar=conversiones() #clase que convierte los numeros a enteros y las letras a minusculas      
        
    #metodo que busca todos los apartamentos y habitaciones que se encuentran entre un rango de precios especifico
    def consultar_precio(self, precio1,precio2):
        self.lista=[]
        self.precio1=self.validar.convertir_entero(precio1)
        self.precio2=self.validar.convertir_entero(precio2)
        for e in self.cursor.execute('''SELECT a.id_apartamento, a.nombre, a.tipo_alquiler,a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono,
        f.n_dormitorio, f.n_bano, f.amueblado, f.cochera, f.agua, f.luz, f.cable, f.internet,f.limpieza, f.lavanderia, f.comida
        from alquiler a inner join facilidades f on a.id_apartamento=f.id_apartamento where a.precio>=? and a.precio<=? order by precio asc''', (self.precio1,self.precio2,)):
            self.lista.append(e)
        return self.lista

    #busca el nombre de una habitacion o apartamento en especifico
    def consultar_nombre(self, nombre):
        self.lista=[]
        self.nombre=self.validar.convertir_minuscula(nombre)
        for e in self.cursor.execute('''SELECT a.id_apartamento,a.tipo_alquiler,a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono,
        f.n_dormitorio, f.n_bano, f.amueblado, f.cochera, f.agua, f.luz, f.cable, f.internet,f.limpieza, f.lavanderia, f.comida
        from alquiler a inner join facilidades f on a.id_apartamento=f.id_apartamento where a.nombre=? order by precio asc''',(self.nombre,)):
            self.lista.append(e)
        return self.lista
    #falta la parte de google maps
    def consultar_ubicacion(self, ubicacion):
        print 'falta esta parte :D'

#Clase que realiza consultas sobre los apartamentos   
class consultas_apartamento(consultas_general):

    #consulta por el precio de los apartamentos
    def consultar_precio(self, precio1,precio2):
        self.lista=[]
        self.precio1=self.validar.convertir_entero(precio1)
        self.precio2=self.validar.convertir_entero(precio2)
        for e in self.cursor.execute('''SELECT a.id_apartamento, a.nombre, a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono, a.numero_personas,
            f.n_dormitorio, f.n_bano, f.amueblado, f.cochera, f.agua, f.luz, f.cable, f.internet 
            from alquiler a inner join facilidades f on a.tipo_alquiler='apartamento' where a.id_apartamento=f.id_apartamento and a.precio>=? and a.precio<=?
            order by precio asc''', (self.precio1,self.precio2,)):
            self.lista.append(e)

        return self.lista

    #consulta por precio y ubicacion, parte de google maps
    def consultar_precio_ubicacion(self):
        print 'falta esta parte :D'

    #metodo que consulta de acuerdo al precio y las facilidades como:luz,agua,cable,internet,cochera, numero de dormitorios    
    def consultar_precio_facilidades(self,precio1,precio2,n_dormitorios):
        self.lista=[]
        self.precio1=self.validar.convertir_entero(precio1)
        self.precio2=self.validar.convertir_entero(precio2)
        self.dormitorios=self.validar.convertir_entero(n_dormitorios)
        for e in self.cursor.execute('''SELECT a.id_apartamento, a.nombre, a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono, a.numero_personas,
            f.n_dormitorio, f.n_bano, f.amueblado  
            from alquiler a inner join facilidades f on a.tipo_alquiler='apartamento' where a.id_apartamento=f.id_apartamento and  a.precio>=? and a.precio<=? and f.luz='si' and f.agua='si'
            and f.cable='si' and f.internet='si' and f.cochera='si' and f.n_dormitorio>=? order by a.precio asc''', (self.precio1,self.precio2,self.dormitorios,)):
            self.lista.append(e)
        return self.lista

    #metodo que consulta por dos facilidades del apartamento, probar ma;ana
    def consultar_2_facilidades_dormitorio(self, facilidad1,facilidad2):
        self.lista=[]
        self.fac1=self.validar.convertir_minuscula(facilidad1)
        self.fac2=self.validar.convertir_minuscula(facilidad2)
        self.dormitorios=self.validar.convertir_entero(dormitorio)
        if ( self.fac1=='agua' and  self.fac2=='luz'):
            for e in self.cursor.execute('''SELECT a.id_apartamento, a.nombre, a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono, a.numero_personas
                from alquiler a inner join facilidades f on a.tipo_alquiler='apartamento' where a.id_apartamento=f.id_apartamento and luz='si' and agua='si' order by a.precio asc'''):
                self.lista.append(e)
        elif ( self.fac1=='agua' and  self.fac2=='cable'):
            for e in self.cursor.execute('''SELECT a.id_apartamento, a.nombre, a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono, a.numero_personas
                from alquiler a inner join facilidades f on a.tipo_alquiler='apartamento' where a.id_apartamento=f.id_apartamento and agua='si' and cable='si'  order by precio asc'''):
                self.lista.append(e)
        
        elif ( self.fac1=='agua' and  self.fac2=='internet'):
            for e in self.cursor.execute('''SELECT a.id_apartamento, a.nombre, a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono, a.numero_personas
                from alquiler a inner join facilidades f on a.tipo_alquiler='apartamento' where a.id_apartamento=f.id_apartamento and agua='si' and internet='si' order by precio asc'''):
                self.lista.append(e)
        elif ( self.fac1=='cable' and  self.fac2=='internet'):
            for e in self.cursor.execute('''SELECT a.id_apartamento, a.nombre, a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono, a.numero_personas
                from alquiler a inner join facilidades f on a.tipo_alquiler='apartamento' where a.id_apartamento=f.id_apartamento and cable='si' and internet='si' order by precio asc'''):
                self.lista.append(e)        
        return self.lista

#clase que consulta por habitaciones
class consultas_habitacion(consultas_general):

    #metodo que consulta por precio de habitacion
    def consultar_precio(self, precio1,precio2):
        self.lista=[]
        self.precio1=self.validar.convertir_entero(precio1)
        self.precio2=self.validar.convertir_entero(precio2)
        for e in self.cursor.execute('''SELECT a.id_apartamento, a.nombre, a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono, 
            f.n_bano,f.bano_compartido, f.limpieza,f.amueblado, f.comida, f.cochera, f.lavanderia, f.agua, f.luz, f.cable, f.internet 
            from alquiler a inner join facilidades f on a.tipo_alquiler='habitacion' where a.id_apartamento=f.id_apartamento and a.precio>=? and a.precio<=?
            order by precio asc''', (self.precio1,self.precio2,)):
            self.lista.append(e)

        return self.lista 

    #consulta por precio y ubicacion, parte de google maps
    def consultar_precio_ubicacion(self):
        print 'falta esta parte :D'


    #consultas por facilidades basicas: luz, agua, telefono, cable...
    def consultar_precio_facilidades(self,precio1,precio2):
        self.lista=[]
        self.precio1=self.validar.convertir_entero(precio1)
        self.precio2=self.validar.convertir_entero(precio2)
        for e in self.cursor.execute('''SELECT a.id_apartamento, a.nombre, a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono,
            f.n_bano, f.amueblado, f.bano_compartido, f.limpieza, f.comida, f.cochera,f.lavanderia  
            from alquiler a inner join facilidades f on a.tipo_alquiler='habitacion' where a.id_apartamento=f.id_apartamento and  a.precio>=? and a.precio<=? and f.luz='si' and f.agua='si'
            and f.cable='si' and f.internet='si' order by a.precio asc''', (self.precio1,self.precio2,)):
            self.lista.append(e)
        return self.lista

    #consultas por facilidades: limpieza, comida y lavanderia
    def consultar_3_facilidades(self):
        self.lista=[]
        for e in self.cursor.execute('''SELECT a.id_apartamento, a.nombre, a.descripcion, a.ubicacion,a.precio,a.correo,a.telefono,
            f.n_bano, f.amueblado, f.bano_compartido,f.cochera, f.agua, f.luz, f.cable, f.internet  
            from alquiler a inner join facilidades f on a.tipo_alquiler='habitacion' where a.id_apartamento=f.id_apartamento and f.lavanderia='si' 
            and f.limpieza='si' and f.comida='si' order by a.precio asc'''):
            self.lista.append(e)
        return self.lista
 
