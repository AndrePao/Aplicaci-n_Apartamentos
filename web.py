from flask import Flask, render_template, request, redirect, url_for, abort, session
import Clase_Alquiler
import PruebaFace

app = Flask(__name__)
#Pagina principal
@app.route('/')
def home():
    return render_template('index.html')

#
@app.route('/Facebook', methods=['POST'])
def Facebook():
    Usuario= request.form['Usuario']
    Contrasena= request.form['Password']
    if PruebaFace.Login_Facebook(Usuario, Contrasena):
	
    	return render_template('index.html')
    else: 
    	return render_template('Login.html')


@app.route('/Publicar')
def Publicar():

    return render_template('Publicar.html')

#Funcion que redirige la pagina para que el usuario elija el tipo de alquiler
@app.route('/Tipo_Alquiler')
def Tipo_Alquiler():

    return render_template('Tipo_Alquiler.html')


@app.route('/Habitacion')
def Habitacion():

    return render_template('Publica_Habitacion.html')


@app.route('/Apartamento')
def Apartamento():

    return render_template('Publica_Apartamento.html')


#Funcion que recibe los parametros de insercion de una habitacion y los envia a la funcion que los almacena en la base
@app.route('/Agrega_Habitacion',  methods=['POST'])
def Agrega_Habitacion():
#Text y numbers
    Nombre= request.form['nombre']
    Ubicacion= request.form['ubicacion']
    Descripcion= request.form['descripcion']
    Email= request.form['email']
    Precio= request.form['precio1']
    Cuartos= request.form['cuartos']
    Banos= request.form['banos']
    Telefono= request.form['telefono']
    Personas= request.form['personas']


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
	
    Agregar= Clase_Alquiler.Habitacion(Nombre, Ubicacion, Precio, Correo, Telefono, Descripcion, )
    return render_template('index.html')

#Funcion que recibe los parametros de insercion de un apartamento y los envia a la funcion que los almacena en la base
@app.route('/Agrega_Apartamento',  methods=['POST'])
def Agrega_Apartamento():
#Text y numbers
    Nombre= request.form['nombre']
    Ubicacion= request.form['ubicacion']
    Descripcion= request.form['descripcion']
    Email= request.form['email']
    Precio= request.form['precio1']
    Cuartos= request.form['cuartos']
    Banos= request.form['banos']
    Telefono= request.form['telefono']
    Personas= request.form['personas']


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

    return render_template('index.html')

@app.route('/Buscar')
def Buscar():

    return render_template('home.html')


@app.route('/Favoritos')
def Favoritos():
    return render_template('home.html')




if __name__ == '__main__':
    app.run()



