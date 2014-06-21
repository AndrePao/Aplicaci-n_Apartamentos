import sqlite3

#CREACION DE LA BASE DE DATOS
conn=sqlite3.connect('Tarea_Lenguajes4.db')
cur=conn.cursor()
#CREACION DE LAS TABLAS QUE SE ENCUENTRAN EN LA BASE DE DATOS
#TABLA USUARIO, ALMACENA LA INFORMACION DE LOS USUARIOS DE LA APLICACION
cur.execute('''create TABLE  usuario
(correo text PRIMARY KEY NOT NULL,
nombre text)''')

#TABLA ALQUILER,ALMACENA LA INFORMACION REFERENTE A ALQUILERES
cur.execute ('''create TABLE  alquiler
(id_apartamento int PRIMARY KEY NOT NULL,
nombre text,
tipo_alquiler text,
descripcion text,
ubicacion text,
precio numeric,
correo text,
telefono text,
numero_personas int)''')

#TABLA FACILIDADES, ALMACENA LA INFORMACION DE LAS CARACTERISTICAS DE LOS ALQUILERES
cur.execute ('''create TABLE  facilidades
(id_apartamento int,
n_dormitorio int, 
n_bano int,
bano_compartido text,
limpieza text,
amueblado text,
comida text,
lavanderia text,
cochera text,
agua text,
luz text,
cable text,
internet text)''')

#TABLA FAVORITOS, ALMACENA LOS APARTAMENTOS FAVORITOS DE LOS USUARIOS
cur.execute ('''CREATE TABLE favoritos(
id_apartamento int,
correo text)''')

conn.commit() #almacena la informacion en la base de datos
conn.close()  #cierra la base de datos
