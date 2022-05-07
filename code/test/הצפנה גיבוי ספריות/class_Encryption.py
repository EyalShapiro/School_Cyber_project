# לה בשימוש
from Main_Server_Encryption import *

from Client_Server_Encryption import *


def main():
    file = "test.txt"
    # file = "hello.wav"

    Client_Server = Client_Server_Encryption()
    Main_Server = Main_Server_Encryption()
    # print('File is encrypted⇨ ', Client_Server.Encryption_File_Text(file), '\n')
    # print('File is dncrypted⇨', Main_Server.Deciphering_File_Text(file), '\n')
    # print('File is encrypted⇨', Main_Server.Encryption_File_wav(file), '\n')
    # print('File is decrypted⇨ ', Client_Server.Deciphering_File_wav(file), '\n')
    text = "Hello and help"
    text = Client_Server_Encryption.Encryption_String(text)
    print("encrypted string ⇨ ", text)
    text = Main_Server_Encryption.Deciphering_String(text)
    print("decrypted string ⇨ ", text)


if __name__ == '__main__':
    main()
