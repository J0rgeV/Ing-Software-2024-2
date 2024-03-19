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

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/') #localhost:5000/renta/
def ver_registros():
    rentas = session.query(Rentar).all()
    resultado = []
    for rnt in rentas:
        cursor.execute(f"SELECT DATEDIFF (NOW(), '{rnt.fecha_renta}')")
        dias = cursor.fetchone()
        if rnt.dias_de_renta < int(dias[0]):
            print(rnt)
            resultado.append("--->" + str(rnt) + "<---")
    return resultado

#responde a localhost:5000/renta/id/1
@renta_blueprint.route('/id/<int:id_renta>/<string:nombre>') #<tipo:nombre_variable>
def ver_renta_id(id_renta, nombre):
    return f"Se hace el query con el id {id_renta} y el nombre {nombre}"

@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'GET':
        return render_template('add_rent.html')
    else:
        #Obtengo la información del método post.
        cliente = request.form['usuario']
        pelicula = request.form['pelicula']

        cursor.execute(f"SELECT NOW()")
        dia = cursor.fetchone()
        print(dia)
        cursor.execute(f"INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES ({cliente}, {pelicula}, NOW(), {10}, {0})")
        conn.commit()
        return render_template('added.html', cosa="una renta", nombre="n/a", ap_pat="", ap_mat="", correo="10 días", destino="renta")

@renta_blueprint.route('/actualizar', methods=['GET', 'POST'])
def edita_renta():
    if request.method == 'GET':
        return render_template('update_rent.html')
    else:
        #Obtengo la información del método post.
        id = request.form['id']
        nuevoValor = request.form['estatus']

        renta = session.query(Rentar).filter(Rentar.idPelicula == id).first()
        renta.estatus = int(nuevoValor)
        session.add(renta)
        session.commit()
        r = session.query(Rentar).filter(Rentar.idPelicula == id).first()
        return "Resultado del cambio: " + str(r)