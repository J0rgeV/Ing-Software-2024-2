import pymysql
import sqlalchemy as alchemy
from flaskProject.alchemyClasses.Schema import Usuario, Pelicula, Rentar, Base, engine, session

# Establecemos conexión con la base de datos.
conn = pymysql.connect(
    host='localhost',
    user='lab',
    password='Developer123!',
    database='lab_ing_software'
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

def insertar_registro_tablas(nombre : str, aPaterno : str, aMaterno : str, password : str, email : str, profPic, superUser : int, nombrePeli : str, genero : str, duracion : str, inventario : str, fechaRenta : str, diasRenta : int, estatus : int, crsr = cursor):
    """
        Función para insertar un nuevo registro en cada tabla.

        Args:
            nombre: Nombre del usuario.
            aPaterno: Apellido paterno del usuario.
            aMaterno: Apellido materno del usuario.
            password: Contraseña del usuario.
            email: Correo electrónico del usuario.
            profPic: Ruta de la imagen de perfil del usuario.
            superUser: Indica si el usuario es superusuario.
            nombrePeli: Nombre de la película.
            genero: Género de la película.
            duracion: Duración de la película.
            inventario: Cantidad de copias de la película.
            fechaRenta: Fecha de renta de la película.
            diasRenta: Días de renta de la película.
            estatus: Indica si la película está rentada.
            crsr: Cursor de la conexión a la base de datos.
    """
    crsr.execute(f"INSERT INTO usuarios (nombre, apPat, apMat, password, email, profilePicture, superUser) VALUES ('{nombre}', '{aPaterno}', '{aMaterno}', '{password}', '{email}', {profPic}, {superUser})")
    conn.commit()
    id1 = crsr.lastrowid

    crsr.execute(f"INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES ('{nombrePeli}', '{genero}', {duracion},  {inventario})")
    conn.commit()
    id2 = crsr.lastrowid

    q = """INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"""
    crsr.execute(q, (id1, id2, fechaRenta, diasRenta, estatus))
    conn.commit()

# Funcion que filtra la table usuarios a todos los usuarios cuyo apellido termine en alguna cadena especificada.
def filtrar_usrs_apellido(apellido : str, crsr = cursor):
    """
        Función para filtrar la tabla de usuarios a todos los usuarios cuyo apellido termine en alguna cadena especificada.

        Args:
            apellido: Cadena que se usará para filtrar la tabla de usuarios.
            crsr: Cursor de la conexión a la base de datos.
    """
    crsr.execute(f"SELECT * FROM usuarios WHERE apPat LIKE '%{apellido}' OR apMat LIKE '%{apellido}'")
    conn.commit()

# Función que dado el nombre de una película y un género, si dicha película existe, se le cambie el género a dicha película.
def cambiar_genero_pelicula(nombrePeli : str, genero : str, crsr = cursor):
    """
        Función para cambiar el género de una película.

        Args:
            nombrePeli: Nombre de la película.
            genero: Nuevo género por asignar a la película si existe.
            crsr: Cursor de la conexión a la base de datos.
    """
    crsr.execute(f"UPDATE peliculas SET genero = '{genero}' WHERE nombre = '{nombrePeli}'")
    conn.commit()

# Función que elimina todas las rentas anteriores a 3 días a la fecha en que se ejecuta la función.
def eliminar_rentas_tres(crsr = cursor):
    """
        Función para eliminar todas las rentas anteriores a 3 días a la fecha en que se ejecuta la función.

        Args:
            crsr: Cursor de la conexión a la base de datos.
    """
    crsr.execute(f"DELETE FROM rentar WHERE fecha_renta <= DATE_SUB(NOW(), INTERVAL 3 DAY)")
    conn.commit()

if __name__ == "__main__":
    # #Prueba de funciones de la base de datos.
    # with open("persona.jpg", "rb") as image:
    #     f = image.read()
    imagen : bytearray = 12324
        

    # # Insertar un nuevo registro en cada tabla
    print("Insertando un nuevo registro en cada tabla...")
    insertar_registro_tablas("Rosa", "García", "Nolasco", "4330", "RoGala@ggmail.com", imagen, 0, "Avatar", "Ciencia Ficción", "183", "7", "2024-02-23", 10, 0)

    # # Filtrar la tabla de usuarios a todos los usuarios cuyo apellido termine en "ez"
    print("Filtrando la tabla de usuarios a todos los usuarios cuyo apellido termine en 'ez'...")
    filtrar_usrs_apellido("ez")
    resultado = cursor.fetchall()
    for r in resultado:
        print(r)

    # Cambiar el género de la película "El Rey León" a "Animación"
    print("Cambiando el género de la película 'Avatar' a 'Ficción'...")
    cambiar_genero_pelicula("Avatar", "Ficción")
    cursor.execute("SELECT * FROM peliculas WHERE nombre = 'Avatar'")
    resultado = cursor.fetchall()
    print("Resultado:")
    for r in resultado:
        print(r)

    # Eliminar todas las rentas anteriores a 3 días a la fecha en que se ejecuta la función
    print("Eliminando todas las rentas anteriores a 3 días a la fecha en que se ejecuta la función...")
    eliminar_rentas_tres()
    cursor.execute("SELECT * FROM rentar")
    resultado = cursor.fetchall()
    print("Resultado:")
    for r in resultado:
        print(r)

    # Aquí crear un menú para darle al usuario las siguientes opciones:
    # 1. Ver los registros de una tabla.
    # 2. Filtrar los registros de una tabla por id.
    # 3. Actualizar la columna nombre de un registro, o fecha_renta para el caso de la de Renta.
    # 4. Eliminar un registro por id de una tabla o todos los registros.
    
    Base.metadata.create_all(engine)

    ejecutando = True
    
    while (ejecutando):
        print("Menú de opciones:")
        print("1. Ver los registros de una tabla.")
        print("2. Filtrar los registros de una tabla por id.")
        print("3. Actualizar la columna nombre de un registro, o fecha_renta para el caso de la de Renta.")
        print("4. Eliminar un registro por id de una tabla o todos los registros.")
        print("5. Salir.")
        opcion = int(input("Ingrese la opción que desea ejecutar: "))

        subejecutando = True
        if opcion == 1:
            while subejecutando:
                tabla = input("Ingrese la tabla que desea ver: ")
                if tabla == "usuarios":
                    usuario = session.query(Usuario).all()
                    for usr in usuario:
                        print(usr)
                    subejecutando = False
                elif tabla == "peliculas":
                    pelicula = session.query(Pelicula).all()
                    for peli in pelicula:
                        print(peli)
                    subejecutando = False
                elif tabla == "rentar":
                    renta = session.query(Rentar).all()
                    for rnt in renta:
                        print(rnt)
                    subejecutando = False
                else:
                    print("Tabla inválida. Intente de nuevo.")
        elif opcion == 2:
            tabla = input("Ingrese la tabla que desea filtrar: ")
            if tabla == "usuarios":
                id = int(input("Ingrese el id del usuario: "))
                usuario = session.query(Usuario).filter(Usuario.idUsuario == id)
                print("Resultado:")
                for usr in usuario:
                    print(usr)
                subejecutando = False
            elif tabla == "peliculas":
                id = int(input("Ingrese el id de la película: "))
                pelicula = session.query(Pelicula).filter(Pelicula.idPelicula == id)
                print("Resultado:")
                for peli in pelicula:
                    print(peli)
                subejecutando = False
            elif tabla == "rentar":
                id = int(input("Ingrese el id de la renta: "))
                renta = session.query(Rentar).filter(Rentar.idRentar == id)
                print("Resultado:")
                for rnt in renta:
                    print(rnt)
                subejecutando = False
            else:
                print("Tabla inválida. Intente de nuevo.")
        elif opcion == 3:
            while subejecutando:
                tabla = input("Ingrese la tabla que desea actualizar: ")
                if tabla == "usuarios":
                    id = int(input("Ingrese el id del usuario a actualizar: "))
                    nuevoValor = input("Ingrese el nuevo valor para la columna nombre: ")
                    usuario = session.query(Usuario).filter(Usuario.idUsuario == id).first()
                    usuario.nombre = nuevoValor
                    session.add(usuario)
                    session.commit()
                    r = session.query(Usuario).filter(Usuario.idUsuario == id)
                    subejecutando = False
                elif tabla == "peliculas":
                    id = int(input("Ingrese el id de la película a actualizar: "))
                    nuevoValor = input("Ingrese el nuevo valor para la columna nombre: ")
                    pelicula = session.query(Pelicula).filter(Pelicula.idPelicula == id).first()
                    pelicula.nombre = nuevoValor
                    session.add(pelicula)
                    session.commit()
                    r = session.query(Pelicula).filter(Pelicula.idPelicula == id)
                    subejecutando = False
                elif tabla == "rentar":
                    id = int(input("Ingrese el id de la renta a actualizar: "))
                    nuevoValor = input("Ingrese el nuevo valor para la columna fecha_renta: ")
                    renta = session.query(Rentar).filter(Rentar.idRentar == id).first()
                    renta.fecha_renta = nuevoValor
                    session.add(renta)
                    session.commit()
                    r = session.query(Rentar).filter(Rentar.idRentar == id)
                    subejecutando = False
                else:
                    print("Tabla inválida. Intente de nuevo.")
            print("Resultado:")
            for res in r:
                print(res)
        elif opcion == 4:
            while subejecutando:
                tabla = input("Ingrese la tabla que desea eliminar registro/s: ")
                if tabla == "usuarios":
                    id = int(input("Ingrese el id del registro (o -1 para eliminar todos los registros): "))
                    if id == -1:
                        session.query(Usuario).delete()
                        session.commit()
                    else:
                        session.query(Usuario).filter(Usuario.idUsuario == id).delete()
                        session.commit()
                    resultado = session.query(Usuario).all()
                    subejecutando = False
                elif tabla == "peliculas":
                    id = int(input("Ingrese el id del registro (o -1 para eliminar todos los registros): "))
                    if id == -1:
                        session.query(Pelicula).delete()
                        session.commit()
                    else:
                        session.query(Pelicula).filter(Pelicula.idPelicula == id).delete()
                        session.commit()
                    resultado = session.query(Pelicula).all()
                    subejecutando = False
                elif tabla == "rentar":
                    id = int(input("Ingrese el id del registro (o -1 para eliminar todos los registros): "))
                    if id == -1:
                        session.query(Rentar).delete()
                        session.commit()
                    else:
                        session.query(Rentar).filter(Rentar.idRentar == id).delete()
                        session.commit()
                    resultado = session.query(Rentar).all()
                    subejecutando = False
                else:
                    print("Tabla inválida. Intente de nuevo.")
            print("Resultado:")
            if resultado:
                for r in resultado:
                    print(r)
            else:
                print("No hay registros.")
        elif opcion == 5:
            ejecutando = False
        else:
            print("Opción inválida. Intente de nuevo.")

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()