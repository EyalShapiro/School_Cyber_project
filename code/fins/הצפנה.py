# צריך להפעוך למחלקה והזה לבוסיף פנועכה של קובץ שעמה
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
#https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/?ref=rp
from cryptography.fernet import Fernet

#########################קבועים########
fernet = Fernet(Fernet.generate_key())#
#######################################


def Encryption_String(text):
    # הצפנה של טקסט
    global fernet
    encMessage = fernet.encrypt(text.encode())
    return encMessage

#################################################
def Deciphering_String(text):
    # פענוך הצפנה של טקסט
    global fernet
    decMessage = fernet.decrypt(text)
    return decMessage.decode()


if __name__ == '__main__':
    text = 'Hello and help'
    print("original string ⇨ ", text)
    text = Encryption_String(text)
    print("encrypted string ⇨ ", text)
    text = Deciphering_String(text)
    print("decrypted string ⇨ ", text)
