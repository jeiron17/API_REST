from flask import Flask
from .modelos import db, Cancion, Album, Usuario

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial_cancion.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app