from cryptography.fernet import Fernet

# Put this somewhere safe!
f = Fernet(Fernet.generate_key())


def Encrypt_text(text):
    encrypted_text = f.encrypt(bytes(text, "UTF-8"))
    return encrypted_text.decode()


def Decrypt_text(text):
    decrypt_text = f.decrypt(bytes(text, "UTF-8"))
    return decrypt_text.decode()


# Testing
text = "test message"

text = Encrypt_text(text)
print("Encrypted message = ", text)

decrypted_text = Decrypt_text(t)
print("Decrypted message = ", decrypted_text)
