<<<<<<< HEAD
from flask import Flask, request, render_template
import flask

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
=======
# import os
# from flask import Flask, flash, request, redirect, url_for
# from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
>>>>>>> parent of 41b923c (1)

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
import falcon
import falcon.asgi

<<<<<<< HEAD
@app.route('/submit', methods=['POST'])
def submit():
    return 'You entered: {}'.format(request.form['text'])


print(submit())
=======
wsgi_app = falcon.App()
asgi_app = falcon.asgi.App()
>>>>>>> parent of 41b923c (1)
