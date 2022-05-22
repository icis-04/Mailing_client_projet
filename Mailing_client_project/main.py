import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.starttls()

server.login('youremail', password)

msg = MIMEMultipart()
msg['From'] = 'Chidera'
msg['To'] = 'destinationemail'
msg['subject'] = 'Subject of the letter'

with open('message.txt', 'r') as f: #reads message from message.txt file
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'My Cover letter.pdf'
attachment = open(filename, 'rb')
"""line 28 and 29 is used to send files that are not plain text """

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('content-disposition',f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('youremail','destinationemail',text)
