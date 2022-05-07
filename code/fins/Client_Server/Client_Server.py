import socket
from Client_Server_Encryption import *
from File_Data import *

###########################################
client_encryption = Client_Server_Encryption()
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 5001
send_data = File_Data()
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
###########################################


def Receiving_wav(data, filename):
    """
    שומר את מדעיה מתקבל בקובץ wav
    """
    global client_encryption
    with open(client_encryption.Get_Locate()+filename, 'wb') as file:
        file.write()
    return file


def main():
    global ClientSocket, client_encryption, sand_data
    Response = ClientSocket.recv(1024)
    while True:
        # send_message משתנה השולח מידע html
        send_data.Set_File_Name(send_message)  # מתקן את שם קובץ
        send_message = send_data.Read_Data()  # מקבל את מאידה של קובץ או את טקסט
        send_message = client_encryption.Encryption_String(send_message)
        ClientSocket.send(str.encode(send_message))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))


if __name__ == "__main__":
    main()
