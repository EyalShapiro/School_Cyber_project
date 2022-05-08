from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('t.html')


@app.route('/submit', methods=['POST'])
def submit():
    return 'You entered: {}'.format(request.form['text'])


app.run()
