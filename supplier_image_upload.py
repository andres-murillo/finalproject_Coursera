#!/usr/bin/env python3

import os
import requests


# url = "http://localhost/upload/"
url = 'http://demozilla.examplehostingprovider.net/'
images_path = '/home/amurillo/workspace/finalproject_Coursera/supplier-data/images/'

def upload_images(path):
    '''Uploads jpg images to url.'''
    for f in os.listdir(path):
        if f.endswith('.jpeg'):    
            file_complete = path + f
            with open(file_complete, 'rb') as opened:
                r = requests.post(url, files={'file': opened})

def main():
    ''' Main '''
    upload_images(images_path)

if __name__ == '__main__':
    main()
