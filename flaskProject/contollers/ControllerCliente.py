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

cliente_blueprint = Blueprint('cliente', __name__, url_prefix='/cliente')

@cliente_blueprint.route('/') #localhost:5000/cliente/
def ver_registros():
    usuarios = session.query(Usuario).all()
    resultado = []
    for usr in usuarios:
        resultado.append(str(usr))
    return resultado

#responde a localhost:5000/cliente/id/1
@cliente_blueprint.route('/id/<int:id_cliente>/<string:nombre>') #<tipo:nombre_variable>
def ver_cliente_id(id_cliente, nombre):
    return f"Se hace el query con el id {id_cliente} y el nombre {nombre}"

@cliente_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_alumno():
    if request.method == 'GET':
        return render_template('add_user.html')
    else:
        #Obtengo la información del método post.
        nombreCliente = request.form['name']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        contr = request.form['passwd']
        correo = request.form['email']
        imagen: bytearray = 12324
        superu = request.form['superusuario']

        cursor.execute(f"INSERT INTO usuarios (nombre, apPat, apMat, password, email, profilePicture, superUser) VALUES ('{nombreCliente}', '{ap_pat}', '{ap_mat}', '{contr}', '{correo}', {imagen}, {superu})")
        conn.commit()
        return render_template('added.html', cosa="un cliente", nombre=nombreCliente, ap_pat=ap_pat, ap_mat=ap_mat, correo=correo, destino="cliente")

@cliente_blueprint.route('/actualizar', methods=['GET', 'POST'])
def edita_cliente():
    if request.method == 'GET':
        return render_template('update_user.html')
    else:
        #Obtengo la información del método post.
        id = request.form['id']
        campo = request.form['campo']
        nuevoValor = request.form['nuevoval']

        usuario = session.query(Usuario).filter(Usuario.idUsuario == id).first()
        if campo == "nombre":
            usuario.nombre = nuevoValor
        elif campo == "appat":
            usuario.apPat = nuevoValor
        elif campo == "apmat":
            usuario.apMat = nuevoValor
        elif campo == "pass":
            usuario.password = nuevoValor
        elif campo == "email":
            usuario.email = nuevoValor
        elif campo == "rol":
            usuario.superUser = nuevoValor
        session.add(usuario)
        session.commit()
        r = session.query(Usuario).filter(Usuario.idUsuario == id).first()
        return "Resultado del cambio: " + str(r)

@cliente_blueprint.route('/eliminar', methods=['GET', 'POST'])
def elimina_cliente():
    if request.method == 'GET':
        return render_template('delete.html')
    else:
        #Obtengo la información del método post.
        usr = request.form['id']

        estado = session.query(Usuario).filter(Usuario.idUsuario == usr).first()
        if not(estado):
            return "No se realizó la eliminación del cliente ya que nunca existió."
        else:
            cursor.execute(f"DELETE FROM rentar WHERE idUsuario = {usr}")
            conn.commit()

            cursor.execute(f"DELETE FROM usuarios WHERE idUsuario = {usr}")
            conn.commit()
            r = session.query(Usuario).filter(Usuario.idUsuario == usr).first()
            if r is None:
                return "Se realizó la eliminación del cliente."
            else:
                return "No se realizó la eliminación del cliente. Algo pasó..."
