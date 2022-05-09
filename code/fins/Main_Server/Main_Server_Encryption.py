from cryptography.fernet import Fernet
###########################################
f = Fernet(Fernet.generate_key())
# f = Fernet(f"N__Ys89Ct7kVKc65IgCly9l1nTXqOuxsotMZkqty4L4=")

###########################################


class Main_Server_Encryption:
    def __init__(self, locate="code/fins/"):
        """
        locate(str): מיקום הקובץ
        """
        global f
        self.fernet = f
        self.file_key = "file_key.key"
        self.locate = locate

    def Get_Locate(self):  # מחזרית את מיקום הקובץ
        return self.locate

    def Set_Locate(self, location):
        """ הפעולה מקלת שפה או מפתח שפה ועדקן מיקום הקובץ"""

        self.locate = location

    def Decrypt_text(self, text, key):  # str
        """        # פענוך הצפנה של טקסט
        הפעולה מקבלת שם ומתחה
        פענוך את הצפנה של טקסט
        לפי מתחה
        """
        decrypt_text = key.decrypt(bytes(text, "UTF-8"))
        return decrypt_text.decode()

    def Encryption_File_wav(self, file_name):  # file wav RSA
        # מצפין את תןכן הקובץ
        """         מצפין את תןכן הקובץ
         הפעולה מקבלת שם קובץ
         מצפנה את תןכן הקובץ
         לפי מתחה הספירה
         """
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

    #  def Encryption_File_Text(self, name_file):  # file txt RSA
    #     """        # מצפין את תןכן הקובץ
    #     הפעולה מקבלת שם קובץ
    #     מצפנה את תןכן הקובץ
    #     לפי מתחה הספירה
    #       """
    #     l = name_file.split('.')312
    #     if l[-1] != 'txt':
    #         return 'This is Not a correct file'
    #     locate = self.locate
    #     file_key = self.file_key

    #     key = Fernet.generate_key()  # generate encryption key
    #     # write the key in a file of .key extension
    #     with open(locate+file_key, 'wb') as filekey:
    #         filekey.write(key)
    #     # crate instance of Fernet    # and load generated key

    #     fernet = Fernet(key)
    #     # read the file to encrypt
    #     with open(locate+name_file, 'rb') as f:
    #         file = f.read()
    #     # encrypt the file
    #     encrypt_file = fernet.encrypt(file)
    #     # open the file and wite the encryption data
    #     with open(locate+name_file, 'wb') as encrypted_file:
    #         encrypted_file.write(encrypt_file)
    #     data_file = ''
    #     with open(locate+name_file, 'r')as f:  # קורא את כל עמידע של קובץ
    #         data_file = f.read()
    #     return data_file
