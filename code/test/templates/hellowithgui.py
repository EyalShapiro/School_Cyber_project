
from flask import Flask, request, render_template
from collections import namedtuple

Message = namedtuple('Message', ['text'])

app = Flask('thewall')

messages = []

# Decorator defines a route
# http://localhost:5000/


@app.route('/', methods=['GET'])
def index():
    return render_template('code/fins/templates/index.html', messages=messages)


@app.route('/', methods=['POST'])
def add_message():
    msg = Message(request.values['text'])
    messages.append(msg)
    return render_template('code/fins/templates/index.html', messages=messages)


if __name__ == '__main__':
    app.run()
