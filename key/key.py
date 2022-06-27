from cryptography.fernet import Fernet


def generate_key():
    """
        יוצר מפתח ושומר אותו בקובץ
        """
    key = Fernet.generate_key()
    with open('file_key.key', "a+") as key_file:
        pass
    with open('file_key.key', "wb") as key_file:
        key_file.write(key)


if __name__ == '__main__':
    generate_key()
