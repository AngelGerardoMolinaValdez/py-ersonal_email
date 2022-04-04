from cryptography.fernet import Fernet


def get_key():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

def set_key():
    return open("clave.key", "rb").read()

get_key()

clave = set_key()

msg = "TrabajosAngel Molina".encode()

f = Fernet(clave)

encrip = f.encrypt(msg)

desencrip = f.decrypt(encrip)

print("""\n\nStr encriptada: {0}\n\nStr desencriptado: {1}""".format(encrip, desencrip))