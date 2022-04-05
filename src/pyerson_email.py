from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
import smtplib

from os.path import basename
from email.mime.application import MIMEApplication


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


    funcs : object = Builtin()
    excel_workbook : object = Excel()


    workbook_id : str = excel_workbook.open_excel_document(f"{BASEDIR}\\data\\{DEFAULT_DATA_FILE}", "reading_info_email")
    

    total_columns : int = excel_workbook.get_column_count(DEFAULT_SHEET)


    host_email : str = excel_workbook.read_excel_cell(1, INIT_COLUMN_DATA, DEFAULT_SHEET)
    encrypth_password : str = excel_workbook.read_excel_cell(2, INIT_COLUMN_DATA, DEFAULT_SHEET)
    password = funcs.decrypt_text(encrypth_password)


    row_data : int = 4
    receiver_email : List[str] = [
        excel_workbook.read_excel_cell(row_data, index, DEFAULT_SHEET) 
        for index in range(INIT_COLUMN_DATA, total_columns+1) 
        if excel_workbook.read_excel_cell(row_data, index, DEFAULT_SHEET) is not None
    ]


    row_data += 1 
    cc_email : List[str] = [
        excel_workbook.read_excel_cell(row_data, index, DEFAULT_SHEET) 
        for index in range(INIT_COLUMN_DATA, total_columns+1) 
        if excel_workbook.read_excel_cell(row_data, index, DEFAULT_SHEET) is not None       
    ]


    row_data += 2 
    atachaments : List[str] = [
        excel_workbook.read_excel_cell(row_data, index, DEFAULT_SHEET) 
        for index in range(INIT_COLUMN_DATA, total_columns+1) 
        if excel_workbook.read_excel_cell(row_data, index, DEFAULT_SHEET) is not None 
    ]


    row_data += 2 
    subject_email : str = excel_workbook.read_excel_cell(row_data, 2, DEFAULT_SHEET)


    row_data += 1 
    type_body_content : str = excel_workbook.read_excel_cell(row_data, 2, DEFAULT_SHEET)


    row_data += 1 
    body_content : str = excel_workbook.read_excel_cell(row_data, 2, DEFAULT_SHEET)


    excel_workbook.close_current_excel_document()


    # create message object instance
    email_account : object = MIMEMultipart()
    
    os.chdir(BASEDIR)
    os.chdir("data")


    # with open("index.html", "rb") as file:
    #     format += str(file.read())


    email_account['From'] = host_email if type(host_email) != None else None
    
    email_account['To'] = ", ".join(receiver_email) if len(receiver_email) >= 1 else None    

    email_account['Subject'] = subject_email if type(subject_email) != None else None
    
    email_account["Cc"] = ", ".join(cc_email) if len(cc_email) >= 1 else None

    email_account.add_header('Content-Type','text/html')

    
    info_email : List[Any] = [email_account['From'], email_account['To'], email_account["Cc"]]
    me_you_cc : List[Any] = [info for info in info_email if info is not None]

    # add in the message body
    email_account.attach(MIMEText(body_content, type_body_content))
    

    #create server
    try:

        server : object = smtplib.SMTP('smtp.gmail.com: 587')    
    

    except:

        server : object = smtplib.SMTP('smtp.gmail.com: 467')


    finally:
        
        server.starttls()
    

    # for f in atachaments:  

    #     attach = MIMEApplication(open(f, "rb").read())

    #     attach.add_header('Content-Disposition','attachment', filename=f)
        
        
    #     email_account.attach(attach)


    # Login Credentials for sending the mail
    server.login(email_account['From'], password)
    
    
    # send the message via the server.
    server.sendmail(*me_you_cc, email_account.as_string())
    # server.sendmail(email_account['From'], email_account['To'], email_account.as_string())
    

    server.quit()
    

