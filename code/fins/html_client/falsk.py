from flask import Flask, request, render_template
import flask
from flask import *
app = Flask(__name__)


@app.route('vois.html', methods=['POST'])

def index():
    data = request.form
    print(data['username'])
    print(data['password']) 
    return data


app.run(debug=True)
