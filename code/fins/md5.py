from hashlib import md5


def deciphering(text):
    # פענוך הצפנה
    return md5(text.encode()).hexdigest()


def Encryption(text):
    # הצפנה
    return md5(text.encode())


def main():
    t = 'test'
    print(Encryption(t))
    t = Encryption(t)
    print(t)
    t = deciphering(t)
    print(t)


if __name__ == '__main__':
    main()
