from flask import Flask, render_template, request, redirect, url_for, abort, session, g
import Clase_Alquiler
import PruebaFace
import Clase_Base_datos
import Consultas
import Clase_usuario_y_favorito

Usuario=""

def correo (correo):
	global Usuario
        Usuario=correo

app = Flask(__name__)
#Pagina principal

@app.route('/')
def home():
    return render_template('Login.html')

#
@app.route("/mapview2")
def mapview2():
    lat=9.8666667
    lng=-83.91666670000001
    return render_template('Publica_Habitacion.html', lat=lat,lng=lng)


@app.route("/mapview")
def mapview():
    lat=9.8666667
    lng=-83.91666670000001
    return render_template('Publica_Apartamento.html', lat=lat,lng=lng)

@app.route('/Facebook', methods=['POST'])
def Facebook():
    Correo= request.form['Usuario']
    Contrasena= request.form['Password']
    if PruebaFace.Login_Facebook(Correo, Contrasena):
	correo(Correo)
    	return render_template('index.html')
    else: 
    	return render_template('Login.html')
  

def numero_filas():
	Base=Clase_Base_datos.Base_datos_conexion()
	cursor=Base.cursor_conexion()
        c=1
        for e in cursor.execute('''SELECT id_apartamento from alquiler'''):
            c+=1
	print c
        return c



@app.route('/Publicar')
def Publicar():
    return render_template('Publicar.html')



@app.route("/Guardar",methods=['POST'])
def Guardar():
    print 'ccc'    
    Latitud=request.form['La']
    Longitud=request.form['Lo']
    Ubicacion=str(Latitud) + ";;;" +str(Longitud)
    return Ubicacion


@app.route('/Consulta_Apartamento')
def Consulta_Apartamento():
    return render_template('consultas_aparta.html')

#Funcion que redirige la pagina para que el usuario elija el tipo de alquiler
@app.route('/Tipo_Alquiler')
def Tipo_Alquiler():
    return render_template('Tipo_Alquiler.html')

#Facilidades 1
@app.route('/Facilidades1_datos')
def Facilidades1_datos():
    return render_template('datos_f1_aparta.html')

@app.route('/Facilidades1_Apartamento', methods=['POST'])
def Facilidades1_Apartamento():
    Cuartos= request.form['cuartos']
    Precio1= request.form['precio1']
    Precio2= request.form['precio2']
    Consulta= Consultas.consultas_apartamento()
    Lista= Consulta.consultar_precio_facilidades(Precio1,Precio2, Cuartos)
    return render_template('imprime_f1_aparta.html', lista=Lista)

#Facilidades 2
@app.route('/Facilidades2_datos')
def Facilidades2_datos():
    return render_template('datos_f2_aparta.html')

@app.route('/Facilidades2_Apartamento', methods=['POST'])
def Facilidades2_Apartamento():
    Consulta= Consultas.consultas_apartamento()
    agua_luz = request.form.getlist('agua_luz')
    agua_cable = request.form.getlist('agua_cable')
    agua_internet = request.form.getlist('agua_internet')
    cable_internet = request.form.getlist('cable_internet')
    if agua_luz:
	Lista= Consulta.consultar_2_facilidades_dormitorio("agua", "luz")
        return render_template('imprime_f2_aparta.html', lista=Lista)
    elif agua_cable:
	Lista= Consulta.consultar_2_facilidades_dormitorio("agua", "cable")
        return render_template('imprime_f2_aparta.html', lista=Lista)
    elif agua_internet:
	Lista= Consulta.consultar_2_facilidades_dormitorio("agua", "internet")
        return render_template('imprime_f2_aparta.html', lista=Lista)
    elif cable_internet:
	Lista= Consulta.consultar_2_facilidades_dormitorio("cable", "internet")
        return render_template('imprime_f2_aparta.html', lista=Lista)
    else:
 	 return render_template('datos_f2_aparta.html')


@app.route('/Precio_Habitacion_Consulta', methods=['POST'])
def Precio_Habitacion_Consulta():
    Precio1= request.form['precio1']
    Precio2= request.form['precio2']
    Consulta= Consultas.consultas_habitacion()
    Lista= Consulta.consultar_precio(Precio1,Precio2)
    return render_template('imprime_precio_habitacion.html',precio= Precio1, precio2= Precio2, lista= Lista)

@app.route('/Precio_Habitacion_F', methods=['POST'])
def Precio_Habitacion_F():
    Precio1= request.form['precio1']
    Precio2= request.form['precio2']
    Consulta= Consultas.consultas_habitacion()
    Lista= Consulta.consultar_precio_facilidades(Precio1,Precio2)
    return render_template('imprime_precio_facilidades.html',precio= Precio1, precio2= Precio2, lista= Lista)

@app.route('/Precio_Habitacion')
def Precio_Habitacion():
    return render_template('datos_precio_habitacion.html')

@app.route('/Precio_Habitacion2')
def Precio_Habitacion2():
    return render_template('datos_precio_hab2.html')

@app.route('/Precio_datos')
def Precio_datos():
    return render_template('datos_precio_aparta.html')


@app.route('/Consulta_Habitacion')
def Consulta_Habitacion():
    return render_template('consultas_habitacion.html')


@app.route('/Precio_Apartamento', methods=['POST'])
def Precio_Apartamento():
    Precio1= request.form['precio1']
    Precio2= request.form['precio2']
    Consulta= Consultas.consultas_apartamento()
    Lista= Consulta.consultar_precio(Precio1,Precio2)
    return render_template('imprime_precio_aparta.html',precio= Precio1, precio2= Precio2, lista= Lista)

"""@app.route('/Ubicacion_Apartamento')
def Ubicacion_Apartamento():
    
    return render_template('imprime_ubicacion_aparta.html')"""

@app.route('/Habitacion')
def Habitacion():
    return render_template('Publica_Habitacion.html')
    


@app.route('/Apartamento')
def Apartamento():
    return render_template('Pin1.html')
   

    


#Funcion que recibe los parametros de insercion de una habitacion y los envia a la funcion que los almacena en la base
@app.route('/Agrega_Habitacion',  methods=['POST'])
def Agrega_Habitacion():
#Text y numbers
    Nombre= request.form['nombre']
    Nombre1= Nombre.lower()
    
    Descripcion= request.form['descripcion']
    Email= request.form['email']
    Precio= request.form['precio1']
    Cuartos= request.form['cuartos']
    Banos= request.form['banos']
    Telefono= request.form['telefono']
    Personas= request.form['personas']
    Latitud=request.form['La']
    Longitud=request.form['Lo']
    Ubicacion=str(Latitud) + "_" +str(Longitud)
   
#Check box 
    amueblado = request.form.getlist('amueblado')
    cable = request.form.getlist('cable')
    agua = request.form.getlist('agua')
    luz = request.form.getlist('luz')
    internet = request.form.getlist('internet')
    cochera = request.form.getlist('cochera')

#Servicios especiales de habitacion
    limpieza = request.form.getlist('limpieza')
    lavanderia = request.form.getlist('lavanderia')
    comida = request.form.getlist('comida')
    banoC = request.form.getlist('bano')
    
#Las siguientes condiciones definen si el servicio es brindado en el alquiler
#condicion de amueblado
    if amueblado:
	amueblado= "si"
    else:
        amueblado= "no"
#condicion de cable
    if cable:
        cable = "si"
    else:
        cable = "no"
#condicion de agua
    if agua:
        agua = "si"
    else:
        agua = "no"
#condicion de luz
    if luz:
        luz = "si"
    else:
        luz = "no"
#condicion de internet
    if internet:
        internet = "si"
    else:
        internet = "no"
#condicion de cochera
    if cochera:
        cochera = "si"
    else:
        cochera = "no"

#condicion de limpieza
    if limpieza:
        limpieza = "si"
    else:
        limpieza = "no"
#condicion de lavanderia
    if lavanderia:
        lavanderia = "si"
    else:
        lavanderia = "no"
#condicion de comida
    if comida:
        comida = "si"
    else:
        comida = "no"
#condicion de bano compartido
    if banoC:
        banoC = "si"
    else:
        banoC = "no"
	
    
    Agregar_Habitacion_Base= Clase_Alquiler.Facilidades(numero_filas(),Nombre1, "habitacion",Ubicacion, Precio, Email, Telefono, Descripcion,  	   Personas, amueblado, cable, agua, luz, internet, Cuartos, cochera, Banos, banoC, comida, limpieza, lavanderia)
    Agregar_Habitacion_Base.agrega_facilidades()
    Agregar_Habitacion_Base.agrega_alquiler()
    return render_template('index.html')

#Funcion que recibe los parametros de insercion de un apartamento y los envia a la funcion que los almacena en la base
@app.route('/Agrega_Apartamento',  methods=['POST'])
def Agrega_Apartamento():

#Text y numbers
    Nombre= request.form['nombre']
    Nombre= Nombre.lower()
   
    Descripcion= request.form['descripcion']
    Email= request.form['email']
    Precio= request.form['precio1']
    Cuartos= request.form['cuartos']
    Banos= request.form['banos']
    Telefono= request.form['telefono']
    Personas= request.form['personas']
    Latitud=request.form['La']
    Longitud=request.form['Lo']
    Ubicacion=str(Latitud) + "_" +str(Longitud)

#Check box 
    amueblado = request.form.getlist('amueblado')
    cable = request.form.getlist('cable')
    agua = request.form.getlist('agua')
    luz = request.form.getlist('luz')
    internet = request.form.getlist('internet')
    cochera = request.form.getlist('cochera')

    
#Las siguientes condiciones definen si el servicio es brindado en el alquiler
#condicion de amueblado
    if amueblado:
	amueblado= "si"
    else:
        amueblado= "no"
#condicion de cable
    if cable:
        cable = "si"
    else:
        cable = "no"
#condicion de agua
    if agua:
        agua = "si"
    else:
        agua = "no"
#condicion de luz
    if luz:
        luz = "si"
    else:
        luz = "no"
#condicion de internet
    if internet:
        internet = "si"
    else:
        internet = "no"
#condicion de cochera
    if cochera:
        cochera = "si"
    else:
        cochera = "no"

	
    Agregar_Apartamento_Base= Clase_Alquiler.Facilidades(numero_filas(),Nombre, "apartamento",Ubicacion, Precio, Email, Telefono, Descripcion, Personas, amueblado, cable, agua, luz, internet, Cuartos, cochera, Banos, "no", "no", "no", "no")
    Agregar_Apartamento_Base.agrega_facilidades()
    Agregar_Apartamento_Base.agrega_alquiler()

    return render_template('index.html')

#Funcion para consultar por nombre
@app.route('/Consulta_nombre',  methods=['POST'])
def Consulta_nombre():
    Nombre= request.form['nombre1']
    Nombre1= Nombre.lower()
  
    Consulta= Consultas.consultas_general()
    Lista= Consulta.consultar_nombre(Nombre1)
    return render_template('imprime_nombre.html', lista=Lista, Alquiler=Nombre)
   
    

@app.route('/Consulta_precio',  methods=['POST'])
def Consulta_precio():
    Precio1= request.form['precio1']
    Precio2= request.form['precio2']
    Consulta= Consultas.consultas_general()
    Lista= Consulta.consultar_precio(Precio1,Precio2)
    
    return render_template('imprime_precio.html', lista=Lista, precio=Precio1, precio2=Precio2)
#
#Funcion para salir de la aplicacion
@app.route('/Salir')
def Salir():
    return render_template('Login.html')


@app.route('/Ver_Favorito',  methods=['POST'])
def Ver_Favorito():
    Nombre= request.form['var']
    Nombre1= Nombre.lower()
    Consulta= Consultas.consultas_general()
    Lista= Consulta.consultar_nombre(Nombre1)
    return render_template('imprime_F.html', lista=Lista, Alquiler=Nombre)
#


@app.route('/Consultar_Favoritos')
def Consultar_Favoritos():
 
    Consultar_Favorito= Clase_usuario_y_favorito.Favorito(Usuario)
    
    Lista=Consultar_Favorito.consultar_favorito()
    return render_template('imprime_favoritos.html', lista=Lista)


@app.route('/Favoritos', methods=['POST'] )
def Favoritos():
    ID= request.form['var']
    Agregar_Favorito= Clase_usuario_y_favorito.Favorito(Usuario)
    Agregar_Favorito.agregar_favorito(ID)
    return render_template('busqueda.html')


@app.route('/Nombre')
def Nombre():
    return render_template('nombre_general.html')

@app.route('/Precio')
def Precio():
    return render_template('precio_general.html')

@app.route('/Ubicacion')
def Ubicacion():
    return render_template('ubicacion_general.html')

#Funcion que redirecciona a la pagina de buscar
@app.route('/Buscar')
def Buscar():
    return render_template('busqueda.html')





if __name__ == '__main__':
    app.run()




