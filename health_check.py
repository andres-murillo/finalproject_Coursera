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

import shutil
import psutil
import socket
import emails

cpu_max_threshold = 80.0
mem_min_threshold = 1_048_576 * 2500
disk_min_threshold = 20.0
ip_lhost = '127.0.0.1'

# def range_bytes(size_bytes):
#     return size_bytes / 1_048_576, 'megabytes'

drive = '/'
du = shutil.disk_usage(drive)
mu = psutil.virtual_memory()
cpu_core_count = psutil.cpu_count(logical=False)
cpu_logical_count = psutil.cpu_count(logical=True)
cpu_usage = psutil.cpu_percent(interval=1)
localhost_ip = socket.gethostbyname('localhost')
free_disk_percentage = 100 - ((du.used / du.total) * 100)

From = 'test@mercaprog.com'
To = 'amurillo@mercaprog.com'
Subject_cpuerror = 'Error - CPU usage is over 80%'
Subject_availdiskerror = 'Error - Available disk space is less than 20%'
Subject_availmemerror = 'Error - Available memory is less than 500MB'
Subject_localhosterror = 'Error - localhost cannot be resolved to 127.0.0.1'
Body = 'Please check your system and resolve the issue as soon as possible.'


if cpu_usage >= cpu_max_threshold:
    print('CPU Usage over 80%')
    message = emails.generate_error_report(From, To, Subject_cpuerror, Body)
    emails.send_email(message, From)

if mu.available < mem_min_threshold:
    print('Low memory')
    message = emails.generate_error_report(From, To, Subject_availmemerror, Body)
    emails.send_email(message, From)

if free_disk_percentage < disk_min_threshold:
    print('Disk Full')
    message = emails.generate_error_report(From, To, Subject_availdiskerror, Body)
    emails.send_email(message, From)

if localhost_ip  != ip_lhost:
    print('Localhost not resolved')
    message = emails.generate_error_report(From, To, Subject_localhosterror, Body)
    emails.send_email(message, From)

# print('Space usage for {}:'.format(drive))
# print('Total space in {}: {:.2f} {}'.format(drive, range_bytes(du.total)[0], range_bytes(du.total)[1]))
# print('Free space in  {}: {:.2f} {}'.format(drive, range_bytes(du.free)[0], range_bytes(du.free)[1]))
# print(f'Porcentaje uso disco: {(du.used / du.total) * 100:.2f}%')
# print(f'Free disk %: {100 - ((du.used / du.total) * 100)}')
# print()
#  print('Memory usage:')
# print('Avail memory: {:.2f} {}'.format( range_bytes(mu.available)[0], range_bytes(mu.available)[1]))
# print(f'Memory available in bytes: {mu.available}')
# print()
# print('CPU Statistics:')
# print('CPU Usage %: {}'.format(cpu_usage))
# print()
# print(f'localhost ip: {localhost_ip}')
