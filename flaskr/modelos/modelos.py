from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    albumes = db.relationship('Album', secondary='album_cancion', back_populates='canciones' )

class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(500))
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.String(1000))
    medio = db.Column(db.Enum(Medio))
    usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    canciones = db.relationship('Cancion', secondary='album_cancion', back_populates='albumes')
    __table__args__ = (db.UniqueConstraint('Usuario', 'titulo', name='titulo_unico_album'),)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(128))
    contrasena = db.Column(db.String(128))
    albumes = db.relationship('Album', cascade='all, delete, delete-orphan')


albumes_canciones = db.Table('album_cancion', \
        db.Column('Album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True), \
        db.Column('Cancion_id', db.Integer, db.ForeignKey('cancion.id'), primary_key=True))













