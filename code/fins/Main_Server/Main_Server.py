# ספריות חיצוניות
import socket
from _thread import *
from threading import *
# קבצים שלי

from Main_Server_Encryption import *
from Info import *
from Text_To_Speech import *

###########################################
# Info.Install_in_File('code/fins/Main_Server/requirements.txt')
if Info.Check_Python_Version('3.7.0'):
    print('The Python version could not run the project\n Replace the Python version')
    sys.exit()
server_encryption = Main_Server_Encryption()
text_to_speech = Text_To_Speech('text', location='code/fins/Main_Server/')
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 21
size = 9000000
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')

ServerSocket.listen(Info.Cores_computer())

###########################################


def threaded_client(connection):
    """העפעולה מקבלת משתמש
    בתליכים למשתמשים
    שולחת לו את מעידה של קובץ
    """
    global server_encryption, ThreadCount
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(size)
        data = data.decode('utf-8')
        data = server_encryption.Decrypt_text(data)  # פענוך טקסט
        print('get client text ', data)
        text_to_speech.Set_text(data)
        text_to_speech.Save_Speech()
        filename = text_to_speech.Get_File_Name()
        f = server_encryption.Encryption_File_wav(filename)
        print(f)
        connection.send(f)
    ThreadCount -= 1

    connection.close()


def main():
    global ServerSocket, ThreadCount
    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client, ))
        ThreadCount += 1

        print('Thread Number: ' + str(ThreadCount))
    ServerSocket.close()


if __name__ == "__main__":
    main()
