from cryptography.fernet import Fernet

# Put this somewhere safe!
f = Fernet(Fernet.generate_key())


def generate_key():
    """
        יוצר מפתח ושומר אותו בקובץ
        """
    key = Fernet.generate_key()
    with open('key.key', "wb") as key_file:
        key_file.write(key)


def Encrypt_text(text):  # str
    # הצפנה של טקסט
    global f
    encrypted_text = f.encrypt(bytes(text, "UTF-8"))
    return encrypted_text.decode()


def Decrypt_text(text):  # str
    # פענוך הצפנה של טקסט
    global f
    decrypt_text = f.decrypt(bytes(text, "UTF-8"))
    return decrypt_text.decode()


# Testing
text = "test message"

text = Encrypt_text(text)
print("Encrypted message = ", text)

decrypted_text = Decrypt_text(text)
print("Decrypted message = ", decrypted_text)
# generate_key()
