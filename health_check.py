#!/usr/bin/env python3

# Report an error if CPU usage is over 80%
# Report an error if available disk space is lower than 20%
# Report an error if available memory is less than 500MB
# Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
# Complete the script to check the system statistics every 60 seconds, 
# and in event of any issues detected among the ones mentioned above, 
# an email should be sent with the following content:
# From: automation@example.com
# To: username@example.com
# Replace username with the username given in the Connection Details Panel on the right hand side.
# Subject line:
# Case
# Subject line
# CPU usage is over 80%
# Error - CPU usage is over 80%
# Available disk space is lower than 20%
# Error - Available disk space is less than 20%
# available memory is less than 500MB
# Error - Available memory is less than 500MB
# hostname "localhost" cannot be resolved to "127.0.0.1"
# Error - localhost cannot be resolved to 127.0.0.1
# E-mail Body: Please check your system and resolve the issue as soon as possible.

from email.message import EmailMessage
from fileinput import filename
import os.path
import mimetypes
import smtplib
import shutil
import psutil

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
