from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .modelos import db, Cancion, Album, Usuario

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5172427@127.0.0.1/tutorial_cancion'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    return app