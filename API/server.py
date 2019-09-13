# -*- coding: utf-8 -*-

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/bonjour')
def autre_route():
    return 'Bonjour'

@app.route('/handle_form', methods=['POST'])
def handle_form():
    print(request.form.get('first_name'))
    return 'Bonjour'

@app.route('/projet/<name>')
def projet(name):
    return 'Bonjour '+name

app.run(port=3000, debug=True)