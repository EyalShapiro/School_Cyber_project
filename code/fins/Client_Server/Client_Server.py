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
    global client_encryption, file_name
    with open(client_encryption.Get_Locate()+file_name, 'wb+') as file:
        file.write(f)
    print(file)
    return


def main():
    global ClientSocket, client_encryption, send_data
    Response = ClientSocket.recv(1024)
    while True:
        # send_message משתנה השולח מידע html
        # send_message = 'School_Cyber_project/code/fins/test.docx'
        send_message = 'test.txt'
        send_data.Set_File_Name(send_message)  # מתקן את שם קובץ
        send_message = send_data.Read_Data()  # מקבל את מאידה של קובץ או את טקסט
        send_message = client_encryption.Encrypt_text(send_message)
        ClientSocket.send(str.encode(send_message))
        Response = ClientSocket.recv(1024)
        res = Response.decode()
        print("file 'wav' name received", Receiving_wav(res))


if __name__ == "__main__":
    main()
