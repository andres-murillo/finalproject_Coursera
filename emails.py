#!/usr/bin/env python3

from email.message import EmailMessage
from fileinput import filename
import os.path
import mimetypes
import smtplib

sender = 'test@mercaprog.com'
recipient = 'amurillo@mercaprog.com'
subj = 'Upload Completed - Online Fruit Store'
cuerpo = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
attachment_path = '/home/amurillo/workspace/finalproject_Coursera/report.pdf'

def generate_email(From, To, Subject, Body, Attachment):
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    message = EmailMessage()
    message['From'] = From
    message['To'] = To
    message['Subject'] = Subject
    body = Body
    message.set_content(body)
    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(), \
        maintype = mime_type, \
        subtype = mime_subtype, filename = os.path.basename(attachment_path))
    return message

def send_email(msg):
    mail_server = smtplib.SMTP_SSL('mail.mercaprog.com')
    mail_pass = 'n7L26F4HUf'
    mail_server.login(sender, mail_pass)
    mail_server.send_message(msg)
    mail_server.quit()

def main():
    mensaje = generate_email(From=sender, To=recipient, Subject=subj, Body=cuerpo, Attachment=attachment_path)
    send_email(mensaje)

if __name__ == '__main__':
    main()
