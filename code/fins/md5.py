from hashlib import md5


def deciphering(text):
    # פענוך הצפנה
    #     text = '000005fab4534d05api_key9a0554259914a86fb9e7eb014e4e5d52permswrite'
    return md5(text.encode()).hexdigest()


def Encryption(text):
    # הצפנה
    return md5(text.encode())


def main():
    pass


if __name__ == '__main__':
    main()
