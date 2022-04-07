import cryptocode
from typing import Optional


class Builtin:
    """ 
    Definition:
    ----------
    Clase que contiene los metodos comunmente utilizados en este proyecto.


    Example:
    -------
    >>> from Builtin import Builtin
    >>> funcs : object = Builtin(basedir)

    """
    
    def __init__(self, basedir : str) -> None:
        """ 
        Definition:
        ----------
        Este metodo asigna los valores que pueden ser utilizados en el proyecto.
        Nota: 
        - Estos atributos estan en mayusculas para ser reconocidos. 
        - No se deben modificar estos valores ya que son solo lectura.

        Arguments:
        ---------
        - basedir : str
            1.- La ruta de inicio del proyecto


        Example:
        -------
        >>> from Builtin import Builtin
        >>> funcs : object = Builtin(basedir)

        """
        self.BASEDIR = basedir


    def encrypt_text(self, text : str) -> str:
        """ 
        Definition:
        ----------
        Encripta una cadena de texto con el modulo cryptocode.


        Arguments:
        ---------
        - text : str
            1. La cadena de caracteres.


        Example:
        -------
        >>> import cryptocode
        >>> encrypt_value = encrypt_text("Hola Mundo")
        >>> print(encrypt_value)
        

        Output:
        ------
        ... K0Le5sMTV4lmBd6q*VyWz8hVzB7VIfeYeZqIHyw==*zmqkGSLqBJEESWXletsoXg==*tHp56v162UTeZv3iYga2lw==
        
        """
        encrypt_text : str = cryptocode.encrypt(text,"wow")

        return encrypt_text


    def decrypt_text(self, text : str) -> str:
        """ 
        Definition:
        ----------
        Desencripta una cadena de texto con el modulo cryptocode.


        Arguments:
        ---------
        - text : str
            1. La cadena de caracteres.


        Example:
        -------
        >>> import cryptocode
        >>> encrypt_value = decrypt_text("K0Le5sMTV4lmBd6q*VyWz8hVzB7VIfeYeZqIHyw==*zmqkGSLqBJEESWXletsoXg==*tHp56v162UTeZv3iYga2lw==")
        >>> print(encrypt_value)
        

        Output:
        ------
        ... Hola Mundo
        
        """
        decrypt_text : str = cryptocode.decrypt(text,"wow")
        
        return decrypt_text


        





