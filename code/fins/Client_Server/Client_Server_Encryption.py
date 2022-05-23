# Client_Server_Encryption.py
from cryptography.fernet import Fernet
###########################################
f = Fernet(Fernet.generate_key())

###########################################


class Client_Server_Encryption:
    def __init__(self, locate="fins/Client_Server/"):
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

    def Load_Key(self):
        """
        טוען את המפתח שנוצר קודם לכן
        """
        # return open(self.locate+self.file_key, "rb").read()
        with open(self.file_key, 'rb+') as filekey:
            key = filekey.read()
        return key

    def Get_Locate(self):
        """
        מחזיר את מיקום הקובץ
        """
        return self.locate

    def Set_Locate(self, location):
        """ 
        הפעולה מקבלת מיקום של הקובץ ומעדכנת אותו
        """

        self.locate = location

    def Encrypt_text(self, text):  # str
        """        # הצפנה של טקסט
        הפעולה מקבלת שם של קובץ wav
        מפענחת את תוכן הקובץ לפי מפתח הספריה 
        ומחזירה את תוכן הקובץ המפוענח
        """
        f = Fernet(self.Load_Key())
        encrypted_text = f.encrypt(bytes(text, "UTF-8"))
        return encrypted_text.decode()

    def Deciphering_File_wav(self, name_file):  # file wav
        """
        הפעולה מקבלת שם של קובץ wav
        מפענחת את תוכן הקובץ לפי מפתח הספריה
        ומחזירה את תוכן הקובץ המפוענח
        """
        l = name_file.split('.')
        if l[-1] != 'wav':
            return 'This is Not a correct file'
        locate = self.locate
        file_key = self.file_key
        key = self.Load_Key()
        with open(locate+file_key, 'rb+') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open(locate+name_file, 'rb') as f:
            file = f.read()
        decrypt_file = fernet.decrypt(file)
        with open(locate+'static/'+name_file, 'wb+') as decrypted_file:
            decrypted_file.write(decrypt_file)
        return decrypt_file  # קורא את כל עמידע של קובץ
