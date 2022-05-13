
from flask import *
from flask import Flask, render_template, request, redirect, url_for

import socket
from Client_Server_Encryption import *
from File_Data import *
from threading import *
from _thread import *

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
    return render_template('index.html')


@app.route('/vois', methods=["POST", "GET"])
def form():
    global send_message
    data = request.form
    if data['text'] != 'תרשום תביעה או בחר קובץ טקסט':
        text = data['text']
    else:
        data = request.files
        file = File_Data(data['upload'].filename)
        text = file.Read_Data()
    send_message = text
    return render_template('vois.html', data=text)


def Thread_App():
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
    print('Running Flask')
    start_new_thread(Thread_App)
    print('Waiting for connection')
    while True:
        #send_data = File_Data()
        # send_message משתנה השולח מידע html
        if send_message != '':
            print('Sending message')
            Response = ClientSocket.recv(size)
            #send_data.Set_File_Name(send_message)  # מתקן את שם קובץ
            #send_message = send_data.Read_Data()  # מקבל את מאידה של קובץ או את טקסט
            # send_message = client_encryption.Encrypt_text(send_message)
            ClientSocket.send(str.encode(send_message))
            Response = ClientSocket.recv(size)
            print(Response)
            print("file 'wav' name received",
                  Receiving_wav(Response))
            send_message = ''


if __name__ == "__main__":
    main()
