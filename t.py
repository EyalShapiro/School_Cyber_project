from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Hey there!"


if __name__ == '__main__':
    app.run(debug=True, host="172.24.48.1", port=443)
