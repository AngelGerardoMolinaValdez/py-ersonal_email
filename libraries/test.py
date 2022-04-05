from cryptography.fernet import Fernet


# def get_key():
#     test = Fernet.generate_key()
#     with open("clave.key", "wb") as archivo_clave:
#         archivo_clave.write(test)

# def set_key():
#     return open("clave.key", "rb").read()

# test = Fernet.generate_key()
# with open("clave.key", "wb") as archivo_clave:
#     archivo_clave.write(test)


# clave = open("clave.key", "rb").read()


# value="TrabajosAngel Molina"
# # clave = Fernet.generate_key()
# f = Fernet(clave)

# print(type(value.encode()))

# encrip = f.encrypt(value.encode())
# print(type(encrip))
# del(archivo_clave)


# test2 = Fernet.generate_key()
# with open("clave2.key", "wb") as archivo_clave2:
#     archivo_clave2.write(test2)


# clave = open("clave2.key", "rb").read()



# desencrip = f.decrypt(encrip)
# print(type(desencrip))


# print("""\n\nStr encriptada: {0}\n\nStr desencriptado: {1}""".format(encrip, desencrip))


# from simplecrypt import encrypt, decrypt
# passkey = 'wow'
# str1 = 'I am okay'
# cipher = encrypt(passkey, str1)
# print(cipher)

import cryptocode

str_encoded = cryptocode.encrypt("TrabajosAngel Molina","wow")
## And then to decode it:
print(str_encoded)

str_decoded = cryptocode.decrypt(str_encoded,"wow")
print(str_decoded)