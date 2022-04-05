import cryptocode
import os
import sys
import base64
from typing import Tuple, List, Dict, Optional, Any, Callable, Union


class Builtin:

    
    def __init__(self) -> None:
        pass


    def encrypt_text(self, encrypt :  str) -> str:
        """ Encripta un mensaje.

        Arguments:
        - encrypt : str
        
        """
        encrypt_text : str = cryptocode.encrypt(encrypt,"wow")

        return encrypt_text


    def decrypt_text(self, decrypt :  str) -> str:
        """ Encripta un mensaje.

        Arguments:
        - encrypt : str
        
        """
        decrypt_text : str = cryptocode.decrypt(decrypt,"wow")
        
        return decrypt_text

    
    def get_type_attach(self, file_name : str) -> Union[str, None]:

        try:

            extension_file : str = file_name.index(".")

            return "MimeImage" if file_name[extension_file+1] in ("png", "jpeg", "jpg") else "MimeText" if file_name[extension_file+1] == "text" else "MimeAplication"


        except:

            return "without_attachment"
        





