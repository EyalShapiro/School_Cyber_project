import socket
import os
from _thread import *
from threading import *

from grpc import server
from Main_Server_Encryption import *
from Info import *
import Text_To_Speech
###########################################
server_encryption = Main_Server_Encryption()
text_to_speech = Text_To_Speech('text', Info)

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 5001
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
"""threading.get_native_id()= New in version 3.8.

החזר את ה-Thread ID
האינטגרלי המקורי של השרשור הנוכחי שהוקצה על ידי הליבה.
⇐======================================================⇒
socket.listen([backlog]):
אפשר לשרת לקבל חיבורים. אם צוין צבר, הוא חייב להיות לפחות 0 (אם הוא נמוך יותר, הוא מוגדר ל-0);
הוא מציין את מספר החיבורים הלא מקובלים שהמערכת תאפשר לפני שתסרב לחיבורים חדשים.
"""
# ServerSocket.listen(Info.Cores_computer())
ServerSocket.listen(4)

###########################################


def Send_Wav(filename):
    """
    מחזר קובץ wav
    מצפן
    """
    global server_encryption
    return server_encryption.Encryption_File_wav(filename)

def threaded_client(connection):
    global server_encryption
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        data=data.decode('utf-8')
        data = server_encryption.Deciphering_String(data)
        reply = 'Server Says: ' + data
        # print(reply)
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()
def Sand_File(filename):
    """
    הפעולה מקבלת קובץ wav
    שולח את קובץ wav
    """
    
    with open(filename, 'rb') as f:
        file = f.read()
    return file
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
