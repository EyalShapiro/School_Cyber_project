from cryptography.fernet import Fernet
###########################################
f = Fernet(Fernet.generate_key())
# f = Fernet(f"N__Ys89Ct7kVKc65IgCly9l1nTXqOuxsotMZkqty4L4=")
###########################################


class Client_Server_Encryption:
    def __init__(self, locate="code/fins/Client_Server/"):
        """
        locate(str): מיקום הקובץ

        """
        global f
        self.fernet = f
        self.file_key = "file_key.key"
        self.locate = locate

    def generate_key(self):
        """
    יוצר מפתח ושומר אותו בקובץ
        """
        key = Fernet.generate_key()
        with open(self.locate+self.file_key, "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        """
    טען את המפתח שנוצר קודם לכן
        """
        with open(self.locate+self.file_key, "wb") as key_file:
            key_file.read()
        return key_file

    def Get_Locate(self):  # מחזרית את מיקום הקובץ
        return self.locate

    def Set_Locate(self, location):
        """ הפעולה מקלת שפה או מפתח שפה ועדקן מיקום הקובץ"""

        self.locate = location

    def Encrypt_text(self, text):  # str
        """        # הצפנה של טקסט
        הפעולה מקבלת שם
        מצפנה את טקסט
        לפי מתחה הספירה
        """
        encrypted_text = f.encrypt(bytes(text, "UTF-8"))
        return encrypted_text.decode()

    def Deciphering_File_wav(self, name_file):  # file wav RSA
        """
        הפעולה מקבלת שם
        מפענוך את תןכן הקובץ
          לפי מתחה הספירה
        """
        l = name_file.split('.')
        if l[-1] != 'wav':
            return 'This is Not a correct file'
        locate = self.locate
        file_key = self.file_key
        key = self.load_key()  # generate encryption key

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
        return decrypt_file  # קורא את כל עמידע של קובץ

    # def Deciphering_File_wav(self, name_file, file_key):  # file wav RSA
    #     # מפענוך את תןכן הקובץ
    #     l = name_file.split('.')
    #     if l[-1] != 'wav':
    #         return 'This is Not a correct file'
    #     locate = self.locate
    #     # file_key = self.file_key
    #     key = Fernet.generate_key()  # generate encryption key
    #     # read the key
    #     with open(locate+file_key, 'rb+') as filekey:
    #         key = filekey.read()
    #     # crate instance of Fernet
    #     # with encryption key
    #     fernet = Fernet(key)
    #     # read the file to decrypt
    #     with open(locate+"encrypted_"+name_file, 'rb') as f:
    #         file = f.read()
    #     # decrypt the file
    #     decrypt_file = fernet.decrypt(file)
    #     # open the file and wite the encrypted data
    #     with open(locate+name_file, 'wb+') as decrypted_file:
    #         decrypted_file.write(decrypt_file)
    #     return decrypt_file  # קורא את כל עמידע של קובץ
