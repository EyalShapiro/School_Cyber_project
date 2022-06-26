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
text_to_speech = Text_To_Speech("")
ServerSocket = socket.socket()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
host = socket.gethostbyname(hostname)
port = 21
size = 9000000
ThreadCount = 0
server_run = True  # הוא רץ True כל עוד זה
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))
# print("host\n ip: ", host, "port:", port)
print('Waitiing for a Connection..')

ServerSocket.listen(Info.Cores_Computer())

###########################################


def threaded_client(connection):
    """העפעולה מקבלת משתמש
    בתליכים למשתמשים
    שולחת לו את מעידה של קובץ
    """
    global server_encryption, ThreadCount
    connection.send(str.encode('Welcome to the Servern'))
    client_run = True  # הוא רץ True כל עוד זה

    while client_run:
        data = connection.recv(size)
        data = data.decode('utf-8')
        data = server_encryption.Decrypt_text(data)  # פענוך טקסט
        print('get client text ', data)
        text_to_speech.Set_Text(data)
        text_to_speech.Save_Speech()
        filename = text_to_speech.Get_File_Name()
        data_file = server_encryption.Encryption_File_wav(
            filename)
        print(data_file)
        connection.send(data_file)
        print('\t↢server sand:)↣ \n')
    ThreadCount -= 1
    connection.close()


def main():
    global ServerSocket, ThreadCount, server_run
    while server_run:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client, ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSocket.close()


if __name__ == "__main__":
    main()
