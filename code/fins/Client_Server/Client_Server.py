import socket
from Client_Server_Encryption import *
from File_Data import *
###########################################
client_encryption = Client_Server_Encryption()
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233
###########################################

def main():
    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    Response = ClientSocket.recv(1024)
    while True:
        send_message = input('Say Something: ')
        send_message=client_encryption.Encryption_String(send_message)
        ClientSocket.send(str.encode(send_message))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))


if __name__ == "__main__":
    main()
