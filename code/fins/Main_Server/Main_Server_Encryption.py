#Main_Server_Encryption.py
from cryptography.fernet import Fernet
###########################################
f = Fernet(Fernet.generate_key())

###########################################


class Main_Server_Encryption:
    def __init__(self, locate="code/fins/Main_Server/"):
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
         הפעולה קאורת את המפתח ומחזרה אותו
        """
        return open(self.locate+self.file_key, "rb").read()

    def Get_Locate(self):  # מחזרית את מיקום הקובץ
        return self.locate

    def Set_Locate(self, location):
        """ הפעולה מקלת שפה או מפתח שפה ועדקן מיקום הקובץ"""

        self.locate = location

    def Decrypt_text(self, text):  # str
        """        # פענוך הצפנה של טקסט
       פעולה מקבלת טקסט מוצפן
        ומצפנה את טקסט
        לפי מפתחה הספירה
        ומחזר את טקסט פענוך
        """
        f = Fernet(self.Load_Key())
        encrypted_text = f.decrypt(bytes(text, "UTF-8"))
        return encrypted_text.decode()

    def Encryption_File_wav(self, file_name):  # file wav RSA
        """
        wav הפעולה מקבלת שם של קובץ
        מצפנה את תןכן הקובץ
        לפי מפתחה הספירה
    ומחזר את תןכן הקובץ מצפנה
        """
        l = file_name.split('.')
        if l[-1] != 'wav':
            return 'This is Not a correct file'
        locate = self.locate
        file_key = self.file_key
        key = self.Load_Key()
        with open(locate+file_key, 'wb') as filekey:
            filekey.write(key)
        fernet = Fernet(key)
        with open(locate+file_name, 'rb') as f:
            file = f.read()
        encrypt_file = fernet.encrypt(file)
        with open(locate+file_name, 'wb') as encrypted_file:
            encrypted_file.write(encrypt_file)
        return encrypt_file  # קורא את כל עמידע של קובץ
