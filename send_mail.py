import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("mail.hashimathman.com", 25)

server.ehlo()

server.login("contact@hashimathman.com", "rQ6X-8w$F1p%qtC")

msg = MIMEMultipart()
msg['From'] = "Hashim"
msg['To'] = "hashimathman.info@gmail.com"
msg['Subject'] = "Testing email send"

with open("message.txt", 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))
filename = 'depot.PNG'
attachment = open(filename, 'rb')

p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header("Content-Disposition", f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('contact@hashimathman.com', 'hashimathman.info@gmail.com', text)