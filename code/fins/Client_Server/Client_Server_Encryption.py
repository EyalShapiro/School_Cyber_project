from cryptography.fernet import Fernet
###########################################
# f = Fernet(Fernet.generate_key())
f = Fernet(f"N__Ys89Ct7kVKc65IgCly9l1nTXqOuxsotMZkqty4L4=")
###########################################


class Client_Server_Encryption:
    def __init__(self, locate="code/fins/"):
        global f
        self.fernet = f
        self.file_key = "file_key.key"
        self.locate = locate

    def Get_Load_Key(self):
        """
        קורא את המפתח מהספרייה הנוכחית בשם 'key.key'
        ומחזיר את מפתח
        """
        with open(self.locate+self.file_key, 'rb+') as filekey:
            key = filekey.read()
        return key

    def Get_Locate(self):  # מחזרית את מיקום הקובץ
        return self.locate

    def Set_Locate(self, location):  # מדקן  את מיקום הקובץ
        self.locate = location

    def Encrypt_text(self, text):  # str
        """        # הצפנה של טקסט
        הפעולה מקבלת שם
        מצפנה את טקסט
        לפי מתחה הספירה
        """
        encrypted_text = f.encrypt(bytes(text, "UTF-8"))
        return encrypted_text.decode()
    def Deciphering_File_wav(self, name_file, file_key):  # file wav RSA
        # מפענוך את תןכן הקובץ
        l = name_file.split('.')
        if l[-1] != 'wav':
            return 'This is Not a correct file'
        locate = self.locate
        # file_key = self.file_key
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
