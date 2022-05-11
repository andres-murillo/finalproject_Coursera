#!/usr/bin/env python3

import os
from PIL import Image

images_path = '/home/amurillo/workspace/finalproject_Coursera/supplier-data/images/'

def convert_images(path):
    ''' Converts .tiff images into .jpeg files,
        also resizes files to 600 x 400 pixels.
    '''
    for f in os.listdir(path):
        if f.endswith('.tiff'):
            i = Image.open(path + f)
            fname, fext = os.path.splitext(f)
            i.convert('RGB').resize((600, 400)).save(path + f'{fname}.jpeg')

def main():
    convert_images(images_path)

if __name__ == '__main__':
    main()
