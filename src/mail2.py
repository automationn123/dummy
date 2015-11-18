import smtplib
fromaddr = 'ravilla.archana@gmail.com'
toaddrs  = 'archana.ravilla@fissionlabs.in'
msg = 'Why,Oh why!'
fileattached = "E:\FL\pdfs\enno.pdf"
username = 'ravilla.archana@gmail.com'
password = 'archana123'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()