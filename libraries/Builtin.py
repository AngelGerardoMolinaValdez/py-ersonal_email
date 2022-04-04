
from cryptography.fernet import Fernet
import os
import sys
from typing import Tuple, List, Dict, Optional, Any, Callable


# def get_key():


# def set_key():
    



# desencrip = f.decrypt(encrip)

# print("""\n\nStr encriptada: {0}\n\nStr desencriptado: {1}""".format(encrip, desencrip))


class Builtin:

    
    def __init__(self) -> None:
        self._set_key()
        self.clave : Any = self._get_key()
        self.Fernet : Fernet = Fernet(self.clave)


    def encrypth_text(self, Str : str) -> str:

        encrypth_text : str = self.Fernet.encrypt(Str.encode())        
        

        return encrypth_text


    def decrypth_text(self, encrypth_text : str) -> str:
        self._set_key()
        self.clave : Any = self._get_key()
        self.Fernet : Fernet = Fernet(self.clave)

        decrypth_text : str = self.Fernet.decrypt(encrypth_text)
        

        return decrypth_text


    def _set_key(self) -> None:

        self.clave = Fernet.generate_key()


        with open("clave.key", "wb") as archivo_clave:

            archivo_clave.write(self.clave)
    

    def _get_key(self) -> Any:
    
        return open("clave.key", "rb").read()

