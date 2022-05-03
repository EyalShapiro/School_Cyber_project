from cryptography.fernet import Fernet


# צריך להפעוך למחלקה והזה לבוסיף פנועכה של קובץ שעמה
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
# https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/?ref=rp
# file txt=https://www.codershubb.com/encrypt-or-decrypt-files-using-python/
#######################################
fernet = Fernet(Fernet.generate_key())
locate = "code/fins/soket/"
file_key = "file_key.key"
#######################################


def Encryption_String(text):  # str
    # הצפנה של טקסט
    global fernet
    encMessage = fernet.encrypt(text.encode())
    return encMessage


def Encryption_File_Text(name_file):  # file txt
    global locate, file_key
    key = Fernet.generate_key()  # generate encryption key
    # write the key in a file of .key extension
    with open(locate+file_key, 'wb') as filekey:
        filekey.write(key)
    # crate instance of Fernet
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
#################################################


def Deciphering_String(text):  # str
    # פענוך הצפנה של טקסט
    global fernet
    decMessage = fernet.decrypt(text)
    return decMessage.decode()


def Deciphering_File_Text(name_file):  # file txt
    global locate, file_key
    # read the key
    with open("code/fins/soket/file_key.key", 'rb+') as filekey:
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
        file = f.read()
    return file


def main():
    print('File is encrypted⇨ ', Encryption_File_Text('test.txt'), '\n')
    print('File is decrypted⇨ ', Deciphering_File_Text('test.txt'), '\n')

    # text = 'Hello and help'
    # print("original string ⇨ ", text)
    # text = Encryption_String(text)
    # print("encrypted string ⇨ ", text)
    # text = Deciphering_String(text)
    # print("decrypted string ⇨ ", text)


if __name__ == '__main__':
    main()
