#!/usr/bin/env python3

import os
from PIL import Image

images_path = '/home/amurillo/workspace/finalproject_Coursera/supplier-data/images/'

for f in os.listdir(images_path):
    if f.endswith('.tiff'):
        i = Image.open(images_path + f)
        fname, fext = os.path.splitext(f)
        i.convert('RGB').resize((600, 400)).save(f'/home/amurillo/workspace/finalproject_Coursera/supplier-data/images/{fname}.jpeg')
