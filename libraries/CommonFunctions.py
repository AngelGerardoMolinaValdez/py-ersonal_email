
import os

import pathlib

from robot.running import TestSuiteBuilder
from robot.model import SuiteVisitor

import random
import datetime
from datetime import timedelta
import pyttsx3  
import pyperclip as clipboard

#import ffmpeg



class CommonFunctions:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LISTENER_API_VERSION = 2
    
    def __init__(self):
        self.list_chars = ['-', '_', '/',',', '|','.','>','*','^','&',';',':']


    def separate_date(self, str_date, type_monts = "abreviado"):
        """Separa dia, mes y año y retorna 3 variables en formato funcional para ingresar en elemento web svg

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${FORMAT_DATE}_       *Separate Date*       _${DATE}_        _${TYPE MONTHS}_
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${DATE}*          _la fecha a convertir en formato soportado para elementos web SVG._
        - *${TYPE MONTHS}*   _El tipo de formato con el que se quieren retornar los meses_
        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${DAY}_  _${MONTH}_  _${YEAR}_  *Separate Date* | 12/12/2021 |
        == RESULTADO ==
        | _${DAY}_   _${MONTH}_   _${YEAR}_  *==*    _12_   _DIC._   _2021_

        == EJEMPLO 2 ==
        | _${DAY}_  _${MONTH}_  _${YEAR}_  *Separate Date* | 09/01/2021 |  completo |
        == RESULTADO ==
        | _${DAY}_   _${MONTH}_   _${YEAR}_  *==*    _9_   _Enero_   _2021_
        """
        str_date =  str_date.replace("/", ",")
        #Separa los datos para almacenar como una lista
        str_date =  str_date.split(",")
        list_date = list(str_date)
        year = str(list_date[2])
        month = str(list_date[1])
        if type_monts.lower() == "abreviado":
            dict_date = {'01':'ENE.','02':'FEB.','03':'MAR.','04':'ABR.','05':'MAY.','06':'JUN.','07':'JUL.','08':'AGO.','09':'SEP.', '10':'OCT.', '11':'NOV.', '12':'DIC.'}
        else:
            dict_date = {'01':'Enero.','02':'Febrero','03':'Marzo','04':'Abril','05':'Mayo','06':'Junio','07':'Julio','08':'Agosto','09':'Septiembre', '10':'Octubre', '11':'Noviembre', '12':'Diciembre'}


        for key, value in dict_date.items(): 
            if month == key: month = value
        # Valida si el primer carater del dia es un 0, si es True retorna solo el segundo digito del dia
        day = str(list_date[0])
        if day[0] == '0': day = day[1]

        return day, month, year



    def get_plain_text(self, str_value):
        """Elimina todos los caracteres diferentes a letras o numeros y retorna la cadena transformada

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${PLAIN_TEXT}_       *Get Plain Text*       _${TEXT}_
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${TEXT}*          _la cadena de texto que se modificara._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${PLAIN_TEXT}_  *Get Plain Text* | $abc25,000  |
        == RESULTADO ==
        | _${PLAIN_TEXT}_  *==*   _abc25000_
        """
        str_plain_value = str(str_value)
        list_chars = []
        list_text = list(str_value)

        for value in list_text:
            ascii_value = ord(value)
            if ascii_value not in range(48, 58):
                    if ascii_value not in range(65, 91):
                            if ascii_value not in range(97, 123): list_chars.append(value) 
        
        for char in list_chars: str_plain_value = str_plain_value.replace(char, "") 

        return str_plain_value



    def get_excel_name(self, str_testname):
        """Ingresa a carpeta testdata y valida que exista un archivo de excel con el nombre ingresado y retorna el nombre del archivo en caso que lo encuentre

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${EXIST}_       *Get Excel Name*       _${TEST_NAME}_
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${TEST_NAME}*          _Nombre que buscara en en la carpeta testdata._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${VAR}_  *Get Excel Name* | template  |
        == RESULTADO ==
        | _${VAR}_  *==*   _template.xlsx_
        """
        path_file = str(os.getcwd())
        os.chdir("..")
        os.chdir("testdata")
        path_file = str(os.getcwd())
        
        fileDir = path_file

        file_not_found = False

        lendir = len(fileDir) + 1


        fileExt = r"*.xlsx"
        fileExt2 = r"*.xls"

        mylistFiles_xlsx = list(pathlib.Path(fileDir).glob(fileExt))
        mylistFiles_xls = list(pathlib.Path(fileDir).glob(fileExt2))

        if len(mylistFiles_xlsx) >= 1:
            for file in mylistFiles_xlsx:

                str_testname =  str_testname.replace("_", "")
                str_testname =  str_testname.replace("-", "")
                str_testname =  str_testname.replace(" ", "")
                str_testname = str_testname.lower()

                name_excel_file = str(file)
                index_extension_file = name_excel_file.index(".")
                name_excel_file = name_excel_file[lendir:index_extension_file]
                name_excel_file =  name_excel_file.replace("_", "")
                name_excel_file =  name_excel_file.replace("-", "")
                name_excel_file =  name_excel_file.replace(" ", "")
                name_excel_file = name_excel_file.lower()

                if len(name_excel_file) < 1:

                    name_excel_file = str(file)
                    name_excel_file = name_excel_file[lendir:]
                    index_extension_file = name_excel_file.index(".")
                    name_excel_file = name_excel_file[:index_extension_file]
                    name_excel_file =  name_excel_file.replace("_", "")
                    name_excel_file =  name_excel_file.replace("-", "")
                    name_excel_file =  name_excel_file.replace(" ", "")
                    name_excel_file = name_excel_file.lower()

                if str_testname == name_excel_file:
                    
                    file_not_found = False
                    excel_file = str(file)
                    index_extension_file = excel_file.index(".") 
                    excel_file = excel_file[lendir:]
                    return excel_file


        if file_not_found:
            if len(mylistFiles_xls) >= 1:
                for file in mylistFiles_xlsx:

                    str_testname =  str_testname.replace("_", "")
                    str_testname =  str_testname.replace("-", "")
                    str_testname =  str_testname.replace(" ", "")
                    str_testname = str_testname.lower()

                    name_excel_file = str(file)
                    index_extension_file = name_excel_file.index(".")
                    name_excel_file = name_excel_file[lendir:index_extension_file]
                    name_excel_file =  name_excel_file.replace("_", "")
                    name_excel_file =  name_excel_file.replace("-", "")
                    name_excel_file =  name_excel_file.replace(" ", "")
                    name_excel_file = name_excel_file.lower()

                    if len(name_excel_file) < 1:

                        name_excel_file = str(file)
                        name_excel_file = name_excel_file[lendir:]
                        index_extension_file = name_excel_file.index(".")
                        name_excel_file = name_excel_file[:index_extension_file]
                        name_excel_file =  name_excel_file.replace("_", "")
                        name_excel_file =  name_excel_file.replace("-", "")
                        name_excel_file =  name_excel_file.replace(" ", "")
                        name_excel_file = name_excel_file.lower()

                    if str_testname == name_excel_file:

                        file_found = str(file)
                        index_extension_file = file_found.index(".") 
                        file_found = file_found[lendir:]
                        return file_found


        
    def delete_extensions(self, name):
        """Elimina la extension de un archivo

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${NEW_NAME}_       *Delete Extensions*       _${NAME}_
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${NAME}*          _Nombre del archivo con extension incluida._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${VAR}_  *Delete Extensions* | template.xlsx  |
        == RESULTADO ==
        | _${VAR}_  *==*   _template_
        """
        index_extension = name.index(".")
        new_name = name[:index_extension]
        return new_name



    def is_test_suite(self):
        """Valida en la carpeta testcases que solo exista una archivo .robot asumiendo asi que es un testsuite

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${IS_TEST_SUITE}_       *Is Test Suite*
 
        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${VAR}_  *Is Test Suite*
        == RESULTADO ==
        | _${VAR}_  *==*   _True_
        """
        path_file = str(os.getcwd())
        fileExt = r"*.robot"
        listFiles = list(pathlib.Path(path_file).glob(fileExt))

        if len(listFiles) > 1: return False 
        else:return True



    def say(self, text, sound_on):
        """Emite voz

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | *Say*       _${TEXT_TO_SAY}_         _${WITH_SOUND}_
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${TEXT_TO_SAY}*          _El texto que emitira la voz._
        - *${WITH_SOUND}*          _Indica si el volumen de la voz es alta o baja._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | *Say* | Hola Mundo!  | True |

        == EJEMPLO 2 ==
        | *Say* | Hola Mundo!  | False  |
        """
        voice = pyttsx3.init() 

        if sound_on is False:
            volume_sound = voice.getProperty('volume')
            voice.setProperty('volume', volume_sound-volume_sound) 
        voice.say(text)  
        voice.runAndWait() 



    def start_with_limit(self, list_values):
        """Separa de una lista de datos y retorna 3 variables diferentes

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${START}_    _${END}_  _${WITH_END}_     *Start With Limit*         _${LIST_DATA}_
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${LIST_DATA}*          _La lista que contiene los valores que seran validados._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${START}_    _${END}_  _${WITH_END}_     *Start With Limit*      | [12-0] |
        == RESULTADO ==
        | _${START}_    _${END}_  _${WITH_END}_   *==*   _12_     _0_      _True_

        """
        char_for_start = ''
        limits = ""

        for value in list_values:
            if value.isnumeric() == False: 
                if value != ' ': char_for_start = value

        for char in self.list_chars:
            if char == char_for_start: limits = list(list_values.split(char))

        if len(limits)>1 and type(limits) is list: start, end, with_end = str(limits[0]), str(limits[1]), bool(1)
        else: start, end, with_end = str(list_values), str(0), bool(0)

        return start, end, with_end


    def repeat_row_n_times(self, list_values):
        """Separa de una lista de datos y retorna 2 variables diferentes

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${START}_    _${END}_     *Repeat Row N Times*         _${LIST_DATA}_
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${LIST_DATA}*          _La lista que contiene los valores que seran validados._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${START}_    _${END}_      *Repeat Row N Times*      | [12-0] |
        == RESULTADO ==
        | _${START}_    _${END}_    *==*   _12_     _0_

        """
        char = ''
        char_for_start = ''
        limits = ""

        for value in list_values:
            if value.isnumeric() == False:
                if value != ' ': char_for_start = value

        for char in self.list_chars:
            if char == char_for_start: limits = list(list_values.split(char))

        start, end = str(limits[0]), str(limits[1])

        return start, end
 


    def convert_text_to(self, type_conversion, text):
        """Cambia el tipo de texto a todas mayusculas, todas minusculas o capitalizado

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${TEXT_CONVERTED}_     *Convert Text To*         _${TEXT}_
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${TYPE_CONVERSION}*          _El tipo de conversion que aplicara a la cadena de texto._
        - *${TEXT}*                      _La cadena que sera manipulada._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${TEXT_CONVERTED}_      *Convert Text To*      | capitalize | hola mundo!! |
        == RESULTADO ==
        | _${TEXT_CONVERTED}_    *==*   _Hola Mundo!!_

        """
        type_conversion = type_conversion.lower()
        type_conversion = type_conversion.strip()

        if "l" == type_conversion == "lower": text = text.lower()
        elif "u" == type_conversion == "upper": text = text.upper()
        elif "c" == type_conversion == "capitalize": text = text.capitalize()
        return text



    def get_message(self, tuple_err):
        """Separa una tupla de datos y retorna uno de ellos

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${MESSAGE}_     *Get Message*         _${TUPLE_DATA}_
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${TUPLE_DATA}*          _la tupla de datos que sera separda._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${MESSAGE}_      *Get Message*      | _("error". "datos")_ | 
        == RESULTADO ==
        | _${MESSAGE}_    *==*   _error_

        """
        tuple_err = tuple(tuple_err)
        value = ""
        
        for i in tuple_err:
            if i is None == False:
                if i.lower() == "debug" or i.lower() == "d" : value =  "debug"
                elif i.lower() == "error" or i.lower() == "e" : value =  "error"
                elif i.lower() == "fatal error" or i.lower() == "fe" : value =  "fatal error"
            else: value =  "None"
        return value



    def string_in_list(self, str_value, list_values):
        """Valida que exista el valor ingresado dentro de la lista de datos

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${EXIST_IN_LIST}_     *String In List*         _${VALUE}_     _${LIST_DATA}_
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${STR_VALUE}*            _El valor que se quiere buscar._
        - *${LIST_VALUES}*          _la lista de datos donde se va a iterar._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${EXIST_IN_LIST}_      *String In List*      | _Si_ |   _['Si', 'NO', 'Si']_ | 
        == RESULTADO ==
        | _${EXIST_IN_LIST}_    *==*   _True_

        """
        list_values = list(list_values)
        str_value = str(str_value)
        value_in_list = False

        for value in list_values:
            if value == str_value: value_in_list = True
        
        return  value_in_list

    

    def decrypt_password(self, str_decrypt):
        """Desencripta la contraseña

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${DECRYPTED_PWD}_     *Decrypt Password*         _${STR_PWD}_    
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${STR_PWD}*            _La contraseña._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${DECRYPTED_PWD}_      *Decrypt Password*      | _116&$%101&$%115&$%116&$%#/=024#/=_ |
        == RESULTADO ==
        | _${DECRYPTED_PWD}_    *==*   _test_

        """
        str_decrypt = str_decrypt[::-1]
        real_index_string = str_decrypt.index("#")
        values_ascii = str_decrypt[:real_index_string]
        list_char_pwd = values_ascii.split("&!%/")
        list_char_pwd.pop()
        str_pwd = ""

        for char in list_char_pwd:
            ascii_value = chr(int(char))
            str_pwd += ascii_value

        return str_pwd



    def get_decorator(self, char):
        """Genera una cadena de texto con un caracter para simular un decorador

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${STRING_DECORATOR}_     *Get Decorator*         _${CHAR}_    
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${CHAR}*            _El tipo de caracter que definira el decorador._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${STRING_DECORATOR}_      *Get Decorator*      | _*_ |
        == RESULTADO ==
        | _${STRING_DECORATOR}_    *==*   _*********************************************************_

        """
        i = 1
        decorator = ""
        while i <= 120:
            i += 1
            decorator += char
                
        return decorator

    def verify_type_value(self, value, type_value):
        """Valida el tipo de una variable

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${TYPE_VAR}_     *Verify Type Value*         _${VALUE}_        _${TYPE_VALUE}_ 
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${VALUE}*                      _La variable que entrara en validacion._
        - *${${EXPECTED TYPE}*            _El tipo de dato que se espera de variable._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${TYPE_VAR}_     *Verify Type Value*      _Hola mundo!_      | _str_ |
        == RESULTADO ==
        | _${TYPE_VAR}_   *==*    _True_

        == EJEMPLO 2 ==
        | _${TYPE_VAR}_      *Verify Type Value*    _Hola mundo!_      | _string_ |
        == RESULTADO ==
        | _${TYPE_VAR}_   *==*    _True_
        """
        type_is_correct = None

        if type_value.lower() in ("str", "string"):
            result_type = type(value)
            if result_type is str:
                type_is_correct = True
            else:
                type_is_correct = False

        elif type_value.lower() in ("int", "integer"):
            result_type = type(value)
            if result_type is int:
                type_is_correct = True
            else:
                type_is_correct = False
        # elif type_value.lower() in ("float"):
        #     result_type = type(value)
        #     if result_type.isnum():
        #         type_is_correct = True

        elif type_value.lower() in ("bool", "boolean"):
            result_type = type(value)
            if result_type is bool:
                type_is_correct = True
            else:
                type_is_correct = False

        elif type_value.lower() in ("list"):
            result_type = type(value)
            if result_type is list:
                type_is_correct = True
            else:
                type_is_correct = False

        elif type_value.lower() in ("dict", "dictionary"):
            result_type = type(value)     
            if result_type is dict:
                type_is_correct = True
            else:
                type_is_correct = False
                
        else:
            type_is_correct = False

        return type_is_correct



    def get_time_for_execution(self, list_times):
        """Valida el tipo de una variable

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | _${TYPE_VAR}_     _${TYPE_VAR_2}_        *Get Time For Execution*         _${VALUE}_   
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${LIST TIMES}*                      _La lista de datos que retornara el tiempo para la ejecucion._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | _${TYPE_VAR}_     _${TYPE_VAR_2}_      *Get Time For Execution*      _[Visible, 2 minutes]_    
        == RESULTADO ==
        | _${TYPE_VAR}_     _${TYPE_VAR_2}_    *==*    _2_       _2 minutes_

        == EJEMPLO 2 ==
        | _${TYPE_VAR}_     _${TYPE_VAR_2}_     *Get Time For Execution*      _[Personalizado, Manual]_    
        == RESULTADO ==
        | _${TYPE_VAR}_     _${TYPE_VAR_2}_   *==*    _-1_        _-1_ 
        """
        list_times = list(list_times)

        selenium_speed = list_times[0] 
        timeout_speed =  list_times[1]

        if selenium_speed == "Rapido":
            selenium_speed = 0

        elif selenium_speed == "Visible":
            selenium_speed = 0.5

        elif selenium_speed == "Lento":
            selenium_speed = 1

        elif selenium_speed == "Muy Lento":
            selenium_speed = 2
        else:
            selenium_speed = -1


        if timeout_speed == "Manual":
            timeout_speed = -1


        return selenium_speed, str(timeout_speed)



    def copy_in_clipboard(self, value):
        """Valida el tipo de una variable

        = ESTRUCTURA =
        == ESTRUCTURA CON VARIABLES ==
        | *Copy In Clipboard*         _${VALUE}_      
        
        = DATOS PARA USABILIDAD =
        Los parametros que recibe en la lista de datos es la siguiente:
        - *${VALUE}*                      _El texto que se pegara en el portapapeles._

        = EJEMPLOS =
        == EJEMPLO 1 ==
        | *Copy In Clipboard*    *Hola mundo!*     |
        """
        clipboard.copy(value)
        #a2 = clipboard.paste()