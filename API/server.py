# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/bonjour')
def autre_route():
    return 'Bonjour'


app.run(port=3000, debug=True)