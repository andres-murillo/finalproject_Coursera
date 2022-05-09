#!/usr/bin/env python3

import os
import requests

filepath = '/home/amurillo/pruebas/files/'

filelist = os.listdir(filepath)

payload = {'title': '', 'name': '', 'date': '', 'feedback': ''}

keys = ['title', 'name', 'date', 'feedback']

def post_dict():
    for textfile in filelist:
        file = filepath + textfile
        with open(file, 'r') as f:
            keynumber = 0
            for line in f.readlines():
                payload[keys[keynumber]] = line.strip()
                keynumber += 1
        resp = requests.post('https://example.com/path/to/api', data=payload)
        print(f'Status code: {resp.status_code}')
        print(resp.text)

def main():
    post_dict()

if __name__ == '__main__':
    main()
