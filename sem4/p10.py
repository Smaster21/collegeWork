from smtplib import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


server=SMTP('smtp.gmail.com',587)
server.starttls()

Youraddr = "Your address"
recaddr = "reciver address"
cc = "reciver address"
bcc = "reciver address"
msg = MIMEMultipart()
msg['From'] = Youraddr
msg['To'] = recaddr
msg['Subject'] = "Subject Of The E-mail"

body = "Your messege"
msg.attach(MIMEText(body,'plain'))

server.login(Youraddr,"Password")
text = msg.as_string()
server.sendmail(Youraddr,[recaddr,cc,bcc],text)
server.quit()

