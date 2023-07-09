from flask import Flask, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import requests
from supplement import get_remedies


app = Flask(__name__)

@app.route('/home', methods =['GET','POST'])
def home():
    if (request.method == 'POST'):
        user_input = request.form.get('upload_form')
        response = get_remedies(user_input)
        response = jsonify({'response': response})
    return render_template('home.html')





@app.route('/', methods =['GET','POST'])
def home2():
    return render_template('home.html')

@app.route('/about', methods = ['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(port = 8005, debug=True)