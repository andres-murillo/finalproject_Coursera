#!/usr/bin/env python3

import os
import requests

img_path = '/home/amurillo/workspace/finalproject_Coursera/supplier-data/images/'
desc_path = '/home/amurillo/workspace/finalproject_Coursera/supplier-data/descriptions/'

desc_filelist = os.listdir(desc_path)

# print(desc_filelist)

payload = {'name': '', 'weight': '', 'description': '', 'image_name':''}

keys = ['name', 'weight', 'description', 'image_name']

def post_dict(filelist, filepath):
    for textfile in filelist:
        img_name = textfile.replace('.txt', '.jpeg')
        file = filepath + textfile
        with open(file, 'r') as f:
            keynumber = 0
            for line in f.readlines():
                payload[keys[keynumber]] = line.strip()
                keynumber += 1
        # resp = requests.post('https://example.com/path/to/api', data=payload)
        # print(f'Status code: {resp.status_code}')
        # print(resp.text)
        payload['image_name'] = img_name
        print(payload)

def main():
    post_dict(desc_filelist, desc_path)

if __name__ == '__main__':
    main()
