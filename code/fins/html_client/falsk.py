from flask import Flask, request, render_template
import flask

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

