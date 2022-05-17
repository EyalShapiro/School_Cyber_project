# Main_Server_Encryption.py
from cryptography.fernet import Fernet
###########################################
f = Fernet(Fernet.generate_key())

###########################################


class E:
    def __init__(self, locate="code/fins/Main_Server/"):
        """
        locate(str): מיקום הקובץ
        """
        global f
        self.fernet = f

        self.file_key = "file_key.key"
        self.locate = locate

    def Load_Key(self):
        """
        הפעולה קאורת את המפתח ומחזרה אותו
        """
        return open(self.locate+self.file_key, "rb").read()

    def Decrypt_text(self, text):  # str
        """        # פענוך הצפנה של טקסט
       פעולה מקבלת טקסט מוצפן
        ומצפנה את טקסט
        לפי מפתחה הספירה
        ומחזר את טקסט פענוך
        """
        f = Fernet(self.Load_Key())
        encrypted_text = f.decrypt(text)
        return encrypted_text.decode()

    def Encrypt_text(self, text):  # str
        """        # הצפנה של טקסט
        הפעולה מקבלת טקסט
        מצפנה את טקסט
        לפי מפתחה הספירה
        ומחזר את טקסט מוצפן
        """
        f = Fernet(self.Load_Key())
        encrypted_text = f.encrypt(text)
        return encrypted_text.decode()


if __name__ == '__main__':
    t = E()
    key = E.Load_Key()
    message = "my deep dark secret".encode()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    # decrypting
    encrypted = b"...encrypted bytes..."
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    m = 'שלום'
    t = E()
    print(m)
    m = t.Encrypt_text(m)
    print(m)
    m = t.Decrypt_text(m)
    print(m)
