import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())


email = EmailMessage()
email['from'] = 'Jeffrey Ho'
email['to'] = 'jeffreytestdev@gmail.com'
email['subject'] = 'This is a testing email'

email.set_content(html.substitute(name= 'TinTin'), 'html') # you can put in dictionary too

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() # tls is an encryption mechanism
    smtp.login('jeffreytestdev@gmail.com', 'Reunion94!')
    smtp.send_message(email)
    print("All good!")