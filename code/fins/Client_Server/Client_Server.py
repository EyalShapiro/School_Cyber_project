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
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
server_host = host  # Main_Server להחליף בלפי
port = 21
size = 9000000
send_message = ''
app = Flask(__name__)
try:  # socket בדיקה של
    ClientSocket.connect((server_host, port))
except socket.error as e:
    print(str(e))  # מדפיס את שגיאת התחברות
###########################################


@app.route('/')
def Home():
    """הפעולה מריצה את אתר"""
    return render_template('index.html')


@app.route('/vois', methods=["POST", "GET"])
def Form():
    """
    הפעולה משתמשת ב
    POST and GET
    כדי לחלץ את המידע מהאתר
    """
    global send_message, client_encryption
    try:
        data = request.form
        message = data['text']  # כתיבת טקסט
        if data['upload'] != None:
            data = request.files
            filename = data['upload'].filename  # העלאת קובץ
            file = File_Data(filename)
            f = file.Read_Data()
        message = message+" "+f
        print('send_message:', message)
    except:
        print('refresh page')
        return Home()  # מרענן את אתר
    send_message = client_encryption.Encrypt_text(message)  # הצפנת הטקסט
    print('send_message:', send_message)
    sleep(8)  # מהשעה את הביצוע למשך מספר 8 השניות

    return render_template('vois.html', data=message)


def Thread_App():
    """
    הפעולה מפעילה  שכדי להריץ את
    Flask
    """
    global app, host
    app.run(debug=False, host=host, threaded=True)
######################################################################


def Receiving_wav(data, filename='say.wav'):
    """
    הפעולה מקבלת את המידע של הקובץ ואת השם שלו
     ושומרת  את המידע  המתקבל בקובץ wav בשל המתקבל
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
    print("The html running from flask now :)\n Waiting for loging to html")
    client_run = True
    while client_run:
        # send_message משתנה השולח מידע html
        if send_message != '':
            print('Sending message')
            Response = ClientSocket.recv(size)
            ClientSocket.send(send_message.encode())
            Response = ClientSocket.recv(size)
            print(Response)
            print("file 'wav' name received", Receiving_wav(Response))
            send_message = ''
    ClientSocket.close()


if __name__ == "__main__":
    main()
