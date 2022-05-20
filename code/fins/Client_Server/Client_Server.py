# ספריות חיצוניות
import socket
from _thread import *
from threading import *
from time import sleep
import flask
from flask import Flask, redirect, render_template, request, url_for
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
file_text = File_Data('')
try:  # socket בדיקה של
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
###########################################


@app.route('/')
def Home():
    """הפעולה מעריץ את אתר"""
    return render_template('index.html')


@app.route('/vois', methods=["POST", "GET"])
def Form():
    """הפעולה עושה
    POST and get
    כדי לקבל את מעדי מי אתר
    ולעכלית איזה סוג היא לוקחת
    ןמעבר לאתר מעמוד בא באתר
    """
    global send_message, client_encryption, file_text
    try:
        data = request.form
        if data['text'] != '':  # כתיבת טקסט
            text = data['text']
        else:  # העלאת קובץ
            data = request.files
            text = data['upload'].filename
            file_text.Set_File_Name(text)
        message = file_text.Read_Data()
        print('send_message:', message)
        send_message = client_encryption.Encrypt_text(message)  # הצפנת הטקסט
        print('send_message:', send_message)
    except:
        print('refresh page')
        return Home()  # מרענן את אתר
    sleep(10)  # מהשעה את הביצוע למשך מספר 10 השניות

    return render_template('vois.html', data=text)


def Thread_App():
    """
    הפעולה מפעילה  שכדי להריץ את
    Flask
    """
    global app
    app.run(debug=False)
###################################


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
    start_new_thread(Thread_App, ())
    sleep(1)  # מהשעה את הביצוע למשך 1 שניות
    print("The html running from flask now :)\n Waiting for connection; )")
    while True:
        # send_message משתנה השולח מידע html
        if send_message != '':
            print('Sending message')
            Response = ClientSocket.recv(size)
            ClientSocket.send(send_message.encode())
            Response = ClientSocket.recv(size)
            print(Response)
            print("file 'wav' name received", Receiving_wav(Response))
            send_message = ''
    connection.close()


if __name__ == "__main__":
    main()
