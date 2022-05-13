import socket
from Client_Server_Encryption import *
from File_Data import *
from http import *
from threading import *
###########################################
client_encryption = Client_Server_Encryption()
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 21
size = 9000000

try:  # soket בדיקה של
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
###########################################


def Receiving_wav(data, filename='say.wav'):
    """
    הפעולה מקלת מעדעי של קובץ ואת שם שלו
    שומר את מדעיה מתקבל בקובץ wav
    """
    global client_encryption
    with open(client_encryption.locate+filename, 'wb+') as file:
        file.write(data)
    decryption = client_encryption.Deciphering_File_wav(
        client_encryption.locate+filename)
    return decryption


def main():
    global ClientSocket, client_encryption, size
    while True:
        send_data = File_Data()
        print('Waiting for connection')
        # send_message משתנה השולח מידע html
        # send_message = 'School_Cyber_project/code/fins/test.docx'
        send_message = 'test.txt'
        if send_message != '':
            Response = ClientSocket.recv(size)
            send_data.Set_File_Name(send_message)  # מתקן את שם קובץ
            send_message = send_data.Read_Data()  # מקבל את מאידה של קובץ או את טקסט
            # send_message = client_encryption.Encrypt_text(send_message)
            ClientSocket.send(str.encode(send_message))
            Response = ClientSocket.recv(size)
            print(Response)
            print("file 'wav' name received",
                  Receiving_wav(Response))
            send_message = ''


if __name__ == "__main__":
    main()
