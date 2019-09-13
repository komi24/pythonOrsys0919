# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from models import db
from models.user import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///peugeot_bdd.sqlite3'


with app.app_context():
    db.init_app(app)
    db.create_all()


#liste_personnes = [
#    {'first_name': 'Toto', 'last_name': 'Martin'},
#    {'first_name': 'Dupont', 'last_name': 'Martine'},
#    {'first_name': 'Durand', 'last_name': 'Helene'},
#]



@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/bonjour')
def autre_route():
    return 'Bonjour'

@app.route('/handle_form', methods=['POST'])
def handle_form():
    print(request.form.get('first_name'))
#    liste_personnes.append({
#        'fisrt_name': request.form.get('first_name'),
#        'last_name': request.form.get('last_name')
#    })
    # Ajouter une personne dans la BDD
    personne = User(
        first_name= request.form.get('first_name'),
        last_name= request.form.get('last_name')
    )
    db.session.add(personne)
    db.session.commit()
    
    # Récupérer toutes les personnes en BDD
    liste_personnes = User.query.all()
    
    return render_template(
            'list.html',
            message="Hello",
            liste_personnes=liste_personnes)

@app.route('/projet/<name>')
def projet(name):
    return 'Bonjour '+name

app.run(port=3000, debug=True)