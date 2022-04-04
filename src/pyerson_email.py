from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


import os
import sys
from typing import Tuple, List, Dict, Optional, Any, Callable


EXCEDIR = os.getcwd()
os.chdir(EXCEDIR)
os.chdir("..")
BASEDIR = os.getcwd()
sys.path.insert(1, BASEDIR)


from libraries.Excel import Excel
from libraries.Builtin import Builtin


def main():

    INIT_COLUMN_DATA : int = 2
    DEFAULT_SHEET : str = "data"
    DEFAULT_DATA_FILE : str = "data.xlsx"


    funcs : Builtin = Builtin()
    excel_workbook : Excel = Excel()


    workbook_id : str = excel_workbook.open_excel_document(f"{BASEDIR}\\data\\{DEFAULT_DATA_FILE}", "reading_info_email")
    

    total_columns : int = excel_workbook.get_column_count(DEFAULT_SHEET)


    host_email : str = excel_workbook.read_excel_cell(INIT_COLUMN_DATA, 2, DEFAULT_SHEET)
    encrypth_password : str = excel_workbook.read_excel_cell(INIT_COLUMN_DATA, 2, DEFAULT_SHEET)
    # decrypth_password : str = funcs.decrypth_text(encrypth_password.encode())

    test = funcs.encrypth_text("test")
    print(test)

    receiver_email : List[str] = [
        excel_workbook.read_excel_cell(4, index, DEFAULT_SHEET) 
        for index in range(INIT_COLUMN_DATA, total_columns+1) 
        if type(excel_workbook.read_excel_cell(4, index, DEFAULT_SHEET)) != None
    ]

    print(receiver_email)


    excel_workbook.close_current_excel_document()




    # # create message object instance
    # msg = MIMEMultipart()
    

    # # *********************************************************************
    # test = ["politronabilene@gmail.com", "alguien39anonino@gmail.com"]
    # message = "Prueba de envio automatico de correo con Python :o"
    
    # # setup the parameters of the message
    # password = "TrabajosAngel Molina"
    # msg['From'] = "angelgerardomolinavaldez@gmail.com"
    # msg['To'] = ", ".join(test)
    # # msg["Cc"] = "serenity@example.com,inara@example.com"
    # # smtp.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
    # msg['Subject'] = "Subscription"
    # # *********************************************************************
    

    # # add in the message body
    # msg.attach(MIMEText(message, 'plain'))
    
    # #create server
    # server = smtplib.SMTP('smtp.gmail.com: 587')
    
    # server.starttls()
    
    # # Login Credentials for sending the mail
    # server.login(msg['From'], password)
    
    
    # # send the message via the server.
    # server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    # server.quit()
    
    # print (f"successfully sent email to:{msg['To']}") 

