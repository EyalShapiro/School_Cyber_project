# ספריות חיצוניות
import flask
from flask import Flask, render_template, request, redirect, url_for
import socket
from threading import *
from _thread import *
from time import sleep
# קבצים שלי

from Client_Server_Encryption import *
from File_Data import *
###########################################
client_encryption = Client_Server_Encryption()
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 21
size = 9000000
send_message = ''
app = Flask(__name__)

try:  # soket בדיקה של
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
###########################################


@app.route('/')
def home():
    """הפעולה מעריץ את אתר"""
    return render_template('index.html')


@app.route('/vois', methods=["POST", "GET"])
def form():
    """הפעולה עושה 
    POST and get
    כדי לקבל את מעדי מי אתר
    ולעכלית איזה סוג היא לוקחת 
    ןמעבר לאתר מעמוד בא באתר
    """
    global send_message, client_encryption
    data = request.form
    if data['text'] != '':
        text = data['text']
    else:
        data = request.files
        file = File_Data(data['upload'].filename)
        text = file.Read_Data()
    send_message = text
    send_message = client_encryption.Encrypt_text(text) #הצפנת הטקסט

    sleep(5)  # מהשעה את הביצוע למשך מספר 5 השניות

    return render_template('vois.html', data=text)


def Thread_App():
    """
    הפעולה מפעילה  שכדי להריץ את
    Flask
    """
    global app
    app.run(debug=False)


def Receiving_wav(data, filename='say.wav'):
    """
    הפעולה מקלת מעדעי של קובץ ואת שם שלו
    שומר את מדעיה מתקבל בקובץ wav
    """
    global client_encryption
    with open(client_encryption.locate+filename, 'wb+') as file:
        file.write(data)
    decryption = client_encryption.Deciphering_File_wav(filename)
    return decryption


def main():
    global ClientSocket, client_encryption, size, send_message
    print('The html running from flask now :)')
    start_new_thread(Thread_App)
    sleep(1)  # מהשעה את הביצוע למשך מספר 1 השניות
    print('Waiting for connection ;)')
    while True:
        # send_message משתנה השולח מידע html
        if send_message != '':
            print('Sending message')
            Response = ClientSocket.recv(size)
            ClientSocket.send(str.encode(send_message))
            Response = ClientSocket.recv(size)
            print(Response)
            print("file 'wav' name received",
                  Receiving_wav(Response))
            send_message = ''


if __name__ == "__main__":
    main()
