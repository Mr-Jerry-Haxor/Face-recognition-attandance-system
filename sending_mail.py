import smtplib, ssl
import pandas as pd   
from datetime import datetime
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "testusermail@gmail.com" #use your mailid
password = "password@123" #use your email password

def send_mail(name):
    attendence_sheet = pd.read_csv("Attendance.csv",index_col="Names")
    student_details = pd.read_csv("student_details.csv",index_col="Name")
    receiver_email = student_details.at[name,'mail']
    attendence_in = attendence_sheet.at[name,'Intime']
    attendence_out = attendence_sheet.at[name,'Outtime']
    # convert time string to datetime
    t1 = datetime.strptime(attendence_in, "%H:%M:%S")
    t2 = datetime.strptime(attendence_out, "%H:%M:%S")
    delta = t2 - t1
    delta = delta.total_seconds()//60
    message = f"""\
    Subject: Face recognition Attendance mail

    This attendance of {name} is {delta} Minutes."""
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    
    
    
    
    
if __name__ == "__main__":
    send_mail('test')

