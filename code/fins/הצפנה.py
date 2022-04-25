import hashlib


def deciphering(text):
    # פענוך הצפנה
    #     text = '000005fab4534d05api_key9a0554259914a86fb9e7eb014e4e5d52permswrite'
    return hashlib.md5(text.encode()).hexdigest()


def Encryption(text):
    # הצפנה
    global list_encry
    return hashlib.md5(text.encode())
