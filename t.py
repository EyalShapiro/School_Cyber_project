from cryptography.fernet import Fernet
###########################################
print(Fernet.generate_key())
k = b'SdftnB2G3UvBQ9XHv1_VI2qQPnG46MiN4QQZ5xx-NdI='
f = Fernet(k)
t = f.encrypt('text'.encode())
print(t)
t = f.decrypt(t)
print(t)
