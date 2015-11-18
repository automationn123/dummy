'''
Created on 18-Mar-2014

@author: ARCHANA
'''
import smtplib,os
from email.MIMEMultipart import MIMEMultipart
from email import Encoders
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
username = 'archana.ravilla@fissionlabs.in'
password = '14112013'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
msg = MIMEMultipart()
msg["Subject"] = "Hi"
msg["From"] = "archana.ravilla@fissionlabs.in"
msg["To"] = "ravilla.archana@gmail.com,sweetyravilla@gmail.com"
msg["Cc"] = "mail2rohitha.123@gmail.com"
body = MIMEText("Hi")
msg.attach(body)
part = MIMEBase('application', "octet-stream")
part.set_payload(open("E:\FL\pdfs\enno.pdf","rb").read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="E:\FL\pdfs\enno.pdf"')
msg.attach(part)
server.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
server.quit()