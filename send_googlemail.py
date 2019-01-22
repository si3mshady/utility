import smtplib
from datetime import datetime 

port = 465
smtp_server = "smtp.gmail.com"
sender_email = 'wayneszalinski82@gmail.com'
recipient = 'si3mshady@gmail.com'
time = str(datetime.now())
msg_dump  = open('latest_system_check').read()
message = "Subject:\n\n{0}\n\n{1}".format(time,msg_dump) #Subject line is filled by supplying Subject and adding (2) new lines 
password = open('contrasena').read().strip()
with smtplib.SMTP_SSL(smtp_server,port) as silver_server:
    silver_server.login(sender_email ,password)
    silver_server.sendmail(sender_email,recipient,message)


