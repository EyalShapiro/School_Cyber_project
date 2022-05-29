# ספריות חיצוניות
import socket
from _thread import *
from threading import *
# קבצים שלי
from Info import *
from Main_Server_Encryption import *
from Text_To_Speech import *


###########################################
Info.Install_in_File('code/fins/Main_Server/requirements.txt')

print("Installing")
if Info.Check_Python_Version('3.7.0'):
    print('The Python version could not run the project\n Replace the Python version')
    sys.exit()
server_encryption = Main_Server_Encryption()
text_to_speech = Text_To_Speech('text', location='fins/Main_Server/')
ServerSocket = socket.socket()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 20
size = 9000000
ThreadCount = 0
server_run = True  # הוא רץ True כל עוד זה

try:
    ServerSocket.bind((ip_address, port))
except socket.error as e:
    print(str(e))  # מדפיס את שגיאת התחברות

print('Waitiing for a Connection')
ServerSocket.listen(Info.Cores_Computer())

###########################################


def threaded_client(connection):
    """
    הפעולה מקבלת משתמש ויוצרת תהליך למשתמשים
    שולחת לו את המידע של קובץ
    """
    global server_encryption, ThreadCount
    connection.send(str.encode('Welcome to the Main_Servern'))
    client_run = True
    while client_run:
        data = connection.recv(size).decode()
        print('get client text ', data)
        text = server_encryption.Decrypt_text(data)  # פענוך טקסט
        print('get client decrypt text  ', text)
        text_to_speech.Set_text(text)
        text_to_speech.Save_Speech()
        filename = text_to_speech.Get_File_Name()
        print('file name', filename)
        file = server_encryption.Encryption_File_wav(filename)
        print('encryption data file: \n', file)
        connection.send(file)
        print("File wav data to sanding")
    print("client connection it is closed ")
    ThreadCount -= 1
    print()
    connection.close()


def main():
    global ServerSocket, ThreadCount, server_run

    while server_run:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client, ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    print("The server is closed")
    ServerSocket.close()


if __name__ == "__main__":
    main()
