from flaskr import create_app
from .modelos import db, cancion , Album , Usuario

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    c = cancion(titulo='prue', minutos=2, segundos=25, interprete='pepe')
    db.session.add(c)
    db.session.commit()
    print(cancion.query.all())

with app.app_context():
    c = Album(tablename='mas', titulo='desde mis hojos', ano=2018, descripcion='cancion que describe las emeociones por la forma en que la mira', medio='CD')
    db.session.add(c)
    db.session.commit()
    print(cancion.query.all())

with app.app_context():
    c = Usuario(tablename='mas', nombre_usuario='patricio', contrasena='patricio123')
    db.session.add(c)
    db.session.commit()
    print(cancion.query.all())