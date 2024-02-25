from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BLOB, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://lab:Developer123!@localhost/lab_ing_software')
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    apPat = Column(String(45))
    apMat = Column(String(45))
    password = Column(String(45))
    email = Column(String(45), unique=True)
    profilePicture = Column(BLOB)
    superUser = Column(Integer)

    def __str__(self):
        return f'IdUsuario: {self.idUsuario}, Nombre Completo: {self.nombre} {self.apPat} {self.apMat}, Contraseña: {self.password}, Correo: {self.email}, SuperUsuario: {self.superUser}'

class Pelicula(Base):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer)

    def __str__(self):
        return f'IdPelicula: {self.idPelicula}, Pelicula: {self.nombre}, Genero: {self.genero} Duracion: {self.duracion}, Inventario: {self.inventario}'

class Rentar(Base):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, primary_key=True)
    idPelicula = Column(Integer, primary_key=True)
    fecha_renta = Column(Date)
    dias_de_renta = Column(Integer)
    estatus = Column(Integer)

    def __str__(self):
        return f'IdRenta: {self.idRentar}, Usuario: {self.idUsuario} Pelicula: {self.idPelicula}, Fecha de renta: {self.fecha_renta}, Dias de renta: {self.dias_de_renta}, Estatus: {self.estatus}'

Session = sessionmaker(engine)
session = Session()