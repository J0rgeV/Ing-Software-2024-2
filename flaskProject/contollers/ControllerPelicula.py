from flask import Blueprint, request, render_template, flash, url_for
from alchemyClasses.Schema import Usuario, Pelicula, Rentar, session
import pymysql

# Establecemos conexión con la base de datos.
conn = pymysql.connect(
    host='localhost',
    user='lab',
    password='Developer123!',
    database='lab_ing_software'
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/') #localhost:5000/pelicula/
def ver_registros():
    peliculas = session.query(Pelicula).all()
    resultado = []
    for flm in peliculas:
        resultado.append(str(flm))
    return resultado

#responde a localhost:5000/pelicula/id/1
@pelicula_blueprint.route('/id/<int:id_pelicula>/<string:nombre>') #<tipo:nombre_variable>
def ver_pelicula_id(id_pelicula, nombre):
    return f"Se hace el query con el id {id_pelicula} y el nombre {nombre}"

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('add_film.html')
    else:
        #Obtengo la información del método post.
        nombrePeli = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inv']

        cursor.execute(f"INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES ('{nombrePeli}', '{genero}', {duracion},  {inventario})")
        conn.commit()
        return render_template('added.html', cosa="una película", nombre=nombrePeli, ap_pat=genero, ap_mat=duracion, correo=inventario, destino="pelicula")

@pelicula_blueprint.route('/actualizar', methods=['GET', 'POST'])
def edita_pelicula():
    if request.method == 'GET':
        return render_template('update_film.html')
    else:
        #Obtengo la información del método post.
        id = request.form['id']
        campo = request.form['campo']
        nuevoValor = request.form['nuevoval']

        pelicula = session.query(Pelicula).filter(Pelicula.idPelicula == id).first()
        if campo == "nombre":
            pelicula.nombre = nuevoValor
        elif campo == "genero":
            pelicula.genero = nuevoValor
        elif campo == "duracion":
            pelicula.duracion = nuevoValor
        elif campo == "inv":
            pelicula.inventario = int(nuevoValor)
        session.add(pelicula)
        session.commit()
        r = session.query(Pelicula).filter(Pelicula.idPelicula == id).first()
        return "Resultado del cambio: " + str(r)

@pelicula_blueprint.route('/eliminar', methods=['GET', 'POST'])
def elimina_pelicula():
    if request.method == 'GET':
        return render_template('delete.html')
    else:
        #Obtengo la información del método post.
        flm = request.form['id']

        estado = session.query(Pelicula).filter(Pelicula.idPelicula == flm).first()
        if not(estado):
            return "No se realizó la eliminación de la película ya que nunca existió."
        else:
            cursor.execute(f"DELETE FROM rentar WHERE idPelicula = {flm}")
            conn.commit()

            cursor.execute(f"DELETE FROM peliculas WHERE idPelicula = {flm}")
            conn.commit()
            r = session.query(Pelicula).filter(Pelicula.idPelicula == flm).first()
            if r is None:
                return "Se realizó la eliminación de la película."
            else:
                return "No se realizó la eliminación de la película. Algo pasó..."
