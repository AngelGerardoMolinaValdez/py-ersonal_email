from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from email.mime.application import MIMEApplication

import os
import sys
from typing import List


EXCEDIR = os.getcwd()
for i in [EXCEDIR, ".."]: os.chdir(i)
BASEDIR = os.getcwd()
sys.path.insert(1, BASEDIR)


from libraries.Excel import Excel
from libraries.Builtin import Builtin


def main():

    INIT_COLUMN_DATA : int = 2
    DEFAULT_SHEET : str = "data"
    DEFAULT_DATA_FILE : str = "data.xlsx"


    funcs : object = Builtin(BASEDIR)
    excel_workbook : object = Excel()


    workbook_id : str = excel_workbook.open_excel_document(f"{BASEDIR}\\data\\{DEFAULT_DATA_FILE}", "reading_info_email")
    

    total_columns : int = excel_workbook.get_column_count(DEFAULT_SHEET)


    host_email : str = excel_workbook.read_excel_cell(1, INIT_COLUMN_DATA, DEFAULT_SHEET)
    type_format_password : str = excel_workbook.read_excel_cell(2, INIT_COLUMN_DATA, DEFAULT_SHEET)
    pwd : str = excel_workbook.read_excel_cell(3, INIT_COLUMN_DATA, DEFAULT_SHEET)
    password = funcs.decrypt_text(pwd) if type_format_password == "encrypted" else pwd


    row_data : int = 5
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
    

    for dir in [BASEDIR, "resources"]: os.chdir(dir)


    if type_body_content:

        file_with_format : str = body_content
        body_content = ""
        
        
        with open(file_with_format, "r") as file:

            body_content += str(file.read())


    email_account['From'] = host_email if type(host_email) != None else None
    email_account['To'] = ", ".join(receiver_email) if len(receiver_email) >= 1 else None    
    email_account['Subject'] = subject_email if type(subject_email) != None else None
    email_account["Cc"] = ", ".join(cc_email) if len(cc_email) >= 1 else None


    email_account.add_header('Content-Type','text/html')


    # add in the message body
    email_account.attach(MIMEText(body_content, type_body_content))
    

    #create server
    try:

        server : object = smtplib.SMTP('smtp.gmail.com: 587')    
    

    except:

        server : object = smtplib.SMTP('smtp.gmail.com: 467')


    finally:
        
        server.starttls()
    
    
    for f in atachaments:  

        attach = MIMEApplication(open(f, "rb").read())

        attach.add_header('Content-Disposition','attachment', filename=f)
        
        email_account.attach(attach)


    # Login Credentials for sending the mail
    server.login(email_account['From'], password)
    
    
    # send the message via the server.
    server.sendmail(email_account['From'], email_account['To'], email_account.as_string())


    server.quit()
    

