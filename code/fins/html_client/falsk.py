from flask import Flask, request, render_template
import flask

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
import falcon
import falcon.asgi

@app.route('/submit', methods=['POST'])
def submit():
    return 'You entered: {}'.format(request.form['text'])


print(submit())
