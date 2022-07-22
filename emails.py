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


def generate_email(From, To, Subject, Body, Attachment):
    message = EmailMessage()
    message['From'] = From
    message['To'] = To
    message['Subject'] = Subject
    body = Body
    message.set_content(body)
    return message

def send_email():
    mail_server = smtplib.SMTP_SSL('mail.mercaprog.com')
    mail_pass = 'n7L26F4HUf'
    mail_server.login(sender, mail_pass)
    mail_server.send_message(message)
    mail_server.quit()

def main():
    generate_email()