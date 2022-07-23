#!/usr/bin/env python3

from email.message import EmailMessage
from fileinput import filename
import os.path
import mimetypes
import smtplib

message = EmailMessage()
sender = 'test@mercaprog.com'
recipient = 'amurillo@mercaprog.com'
attachment_path = '/home/amurillo/workspace/finalproject_Coursera/report.pdf'
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

mail_server = smtplib.SMTP_SSL('mail.mercaprog.com')
mail_pass = 'n7L26F4HUf'

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

body = '''Hey there!

I'm learning to send emails using Python!!'''

message.set_content(body)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), \
    maintype = mime_type, \
    subtype = mime_subtype, filename = os.path.basename(attachment_path))

mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()
