# ספריות חיצוניות
import socket
from _thread import *
from threading import *
from time import sleep
from flask import *
from flask import Flask, redirect, render_template, request, url_for
# קבצים שלי
from Client_Server_Encryption import *
from File_Data import *


###########################################
client_encryption = Client_Server_Encryption()
size = 9000000
ClientSocket = socket.socket()

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
server_host = ip  # Main_Server להחליף בלפי
port = 20
send_message = ''
client_run = True  # הוא רץ True כל עוד זה

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
        data = request.form  # כתיבת טקסט
        text = data['text']
        if data['upload'] != '':
            data = request.files  # העלאת קובץ
            file = File_Data(data['upload'].filename)
            text_file = ''
            file = File_Data(data['upload'].filename)
            text_file = file.Read_Data()
            if message and text_file != '' and text_file != '':
                message = message+" "+text_file
            else:
                message = text_file
        else:
            message = text
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
    global app
    app.run(debug=False, host='0.0.0.0', threaded=True)  # run the app on main
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
    global ClientSocket, client_encryption, send_message, client_run, size
    start_new_thread(Thread_App, ())
    sleep(0.2)  # מהשעה את הביצוע למשך .0.2 שניות
    print("The html running from flask now :)\n Waiting for loging to html")
    while client_run:
        # send_message משת1`נה השולח מידע html
        if send_message != '':
            print('Data Message is not null')
            response = ClientSocket.recv(size)
            print('Received: \f', response)
            ClientSocket.send(send_message.encode())
            response = ClientSocket.recv(size).decode()
            print(response)
            print("file 'wav' name received", Receiving_wav(response))
            send_message = ''
    ClientSocket.close()


if __name__ == "__main__":
    main()
