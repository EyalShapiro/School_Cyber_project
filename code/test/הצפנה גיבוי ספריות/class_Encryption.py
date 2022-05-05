# לה בשימוש
from Main_Server_Encryption import *

from Client_Server_Encryption import *


def main():
    # file="test.txt"

    # print('File is encrypted⇨ ', Encryption_File_Text(file), '\n')
    # print('File is decrypted⇨ ', Deciphering_File_Text(file), '\n')
    Client_Server = Client_Server_Encryption()
    Main_Server = Main_Server_Encryption()
    file = "hello.wav"

    print('File is decrypted⇨ ', Main_Server.Encryption_File_wav(file), '\n')
    print('File is encrypted⇨ ', Client_Server.Deciphering_File_wav(file), '\n')
    # text = 'Hello and help'
    # print("original string ⇨ ", text)
    # text = Encryption_String(text)
    # print("encrypted string ⇨ ", text)
    # text = Deciphering_String(text)
    # print("decrypted string ⇨ ", text)


if __name__ == '__main__':
    main()
