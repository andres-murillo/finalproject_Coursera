#!/usr/bin/env python3

from email.message import EmailMessage
from fileinput import filename
import os.path
import mimetypes
import smtplib

message = EmailMessage()
sender = 'test@mercaprog.com'
recipient = 'amurillo@mercaprog.com'

mail_server = smtplib.SMTP_SSL('mail.mercaprog.com')
mail_pass = 'n7L26F4HUf'

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

body = '''Hey there!

I'm learning to send emails using Python!!'''

message.set_content(body)

mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()

def generate_email():
    pass

def send_email():
    pass

