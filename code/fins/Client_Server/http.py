import os
import flask
from flask import *
from flask import Flask, render_template, request, redirect, url_for
from File_Data import *
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/vois', methods=["POST", "GET"])
def form():
    data = request.form
    if data['text'] != 'תרשום תביעה או בחר קובץ טקסט':
        text = data['text']
    else:
        data = request.files
        file = File_Data(data['upload'].filename)
        text = file.Read_Data()

    return render_template('vois.html', data=text)


if __name__ == '__main__':
    app.run(debug=False)
