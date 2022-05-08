from cryptography.fernet import Fernet
###########################################
f = Fernet(Fernet.generate_key())
# f = Fernet(f"N__Ys89Ct7kVKc65IgCly9l1nTXqOuxsotMZkqty4L4=")

###########################################


class Main_Server_Encryption:
    def __init__(self, locate="code/fins/"):
        global f
        self.fernet = f
        self.file_key = "file_key.key"
        self.locate = locate

    def Get_Locate(self):  # מחזרית את מיקום הקובץ
        return self.locate

    def Set_Locate(self, location):  # מדקן  את מיקום הקובץ
        self.locate = location

    def load_key():
        """
        טוען את המפתח מהספרייה הנוכחית בשם 'key.key'
        """
        return open("key.key", "rb").read()

    def Decrypt_text(self, text, key):  # str
        # פענוך הצפנה של טקסט
        decrypt_text = key.decrypt(bytes(text, "UTF-8"))
        return decrypt_text.decode()

    def Deciphering_File_Text(self, file_key, file_name):  # file txt RSA
        # מפענוך את תןכן הקובץ
        l = file_name.split('.')
        if l[-1] != 'txt':
            return 'This is Not a correct file'
        locate = self.locate
        # read the key
        with open(locate+file_key, 'rb+') as filekey:
            key = filekey.read()
        # crate instance of Fernet        # with encryption key
        fernet = Fernet(key)
        # read the file to decrypt
        with open(locate+file_name, 'rb') as f:
            file = f.read()
        # decrypt the file
        decrypt_file = fernet.decrypt(file)
        # open the file and wite the encrypted data
        with open(locate+file_name, 'wb+') as decrypted_file:
            decrypted_file.write(decrypt_file)
        with open(locate+file_name, 'r')as f:  # קורא את כל עמידע של קובץ
            data_file = f.read()
        return data_file

    def Encryption_File_wav(self, file_name):  # file wav RSA
        # מצפין את תןכן הקובץ
        l = file_name.split('.')
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
        with open(locate+file_name, 'rb') as f:
            file = f.read()
        # encrypt the file
        encrypt_file = fernet.encrypt(file)
        # open the file and wite the encryption data
        with open(locate+"encrypted_"+file_name, 'wb') as encrypted_file:
            encrypted_file.write(encrypt_file)
        return encrypt_file  # קורא את כל עמידע של קובץ
    # def Get_key(self):

    def GenerateKey(self):
        Key = Fernet.generate_key()
        return Key
