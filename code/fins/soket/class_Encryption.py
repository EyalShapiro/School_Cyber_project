# לה בשימוש
from cryptography.fernet import Fernet
#######################################
#######################################


class Client_Server_Encryption:
    fernet = Fernet(Fernet.generate_key())
    file_key = "file_key.key"
    locate = "code/fins/soket/"

    def Encryption_String(self, text):  # str
        # הצפנה של טקסט
        global fernet
        encMessage = fernet.encrypt(text.encode())
        return encMessage

    def Encryption_File_Text(self, name_file):  # file txt RSA
        # מצפין את תןכן הקובץ
        l = name_file.split('.')
        if l[-1] != 'txt':
            return 'This is Not a correct file'
        locate=self.locate
        file_key = self.file_key

        key = Fernet.generate_key()  # generate encryption key
        # write the key in a file of .key extension
        with open(locate+file_key, 'wb') as filekey:
            filekey.write(key)
        # crate instance of Fernet    # and load generated key

        fernet = Fernet(key)
        # read the file to encrypt
        with open(locate+name_file, 'rb') as f:
            file = f.read()
        # encrypt the file
        encrypt_file = fernet.encrypt(file)
        # open the file and wite the encryption data
        with open(locate+name_file, 'wb') as encrypted_file:
            encrypted_file.write(encrypt_file)
        data_file = ''
        with open(locate+name_file, 'r')as f:  # קורא את כל עמידע של קובץ
            data_file = f.read()
        return data_file

    def Deciphering_File_wav(self, name_file):  # file wav RSA
        # מפענוך את תןכן הקובץ
        l = name_file.split('.')
        if l[-1] != 'wav':
            return 'This is Not a correct file'
        locate = self.locate
        file_key = self.file_key
        key = Fernet.generate_key()  # generate encryption key

        # read the key
        with open(locate+file_key, 'rb+') as filekey:
            key = filekey.read()
        # crate instance of Fernet
        # with encryption key
        fernet = Fernet(key)
        # read the file to decrypt
        with open(locate+"encrypted_"+name_file, 'rb') as f:
            file = f.read()

        # decrypt the file
        decrypt_file = fernet.decrypt(file)
        # open the file and wite the encrypted data
        with open(locate+name_file, 'wb+') as decrypted_file:
            decrypted_file.write(decrypt_file)
        return decrypt_file  # קורא את כל עמידע של קובץ

    ##################################################################################################
# ---------------------------------------------------


class Main_Server_Encryption:
    fernet = Fernet(Fernet.generate_key())
    file_key = "file_key.key"
    locate = "code/fins/soket/"

    def Deciphering_String(self, text):  # str
        # פענוך הצפנה של טקסט
        global fernet
        decMessage = fernet.decrypt(text)
        return decMessage.decode()

    def Deciphering_File_Text(self, name_file):  # file txt RSA
        # מפענוך את תןכן הקובץ
        l = name_file.split('.')
        if l[-1] != 'txt':
            return 'This is Not a correct file'
        key = Fernet.generate_key()  # generate encryption key

        locate=self.locate
        file_key = self.file_key
        # read the key
        with open(locate+file_key, 'rb+') as filekey:
            key = filekey.read()
        # crate instance of Fernet
        # with encryption key
        fernet = Fernet(key)
        # read the file to decrypt
        with open(locate+name_file, 'rb') as f:
            file = f.read()

        # decrypt the file
        decrypt_file = fernet.decrypt(file)
        # open the file and wite the encrypted data
        with open(locate+name_file, 'wb+') as decrypted_file:
            decrypted_file.write(decrypt_file)
        file = ''
        with open(locate+name_file, 'r')as f:  # קורא את כל עמידע של קובץ
            data_file = f.read()
        return data_file

    def Encryption_File_wav(self, name_file):  # file wav RSA
        # מצפין את תןכן הקובץ
        l = name_file.split('.')
        if l[-1] != 'wav':
            return 'This is Not a correct file'
        locate = self.locate
        file_key = self.file_key

        key = Fernet.generate_key()  # generate encryption key
        # write the key in a file of .key extension
        with open(locate+file_key, 'wb') as filekey:
            filekey.write(key)
        # crate instance of Fernet    # and load generated key

        fernet = Fernet(key)
        # read the file to encrypt
        with open(locate+name_file, 'rb') as f:
            file = f.read()
        # encrypt the file
        encrypt_file = fernet.encrypt(file)
        # open the file and wite the encryption data
        with open(locate+"encrypted_"+name_file, 'wb') as encrypted_file:
            encrypted_file.write(encrypt_file)
        return encrypt_file  # קורא את כל עמידע של קובץ


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
