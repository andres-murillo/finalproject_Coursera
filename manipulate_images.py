#!/usr/bin/env python3

import os
from PIL import Image

images_path = '/home/amurillo/workspace/finalproject_Coursera/supplier-data/images/'

for f in os.listdir(images_path):
    if f.endswith('.tiff'):
        print(f)

    # if f.endswith('.tiff'):
    #     i = Image.open(f)
    #     fname, ext = os.path.splitext(f)
    #     print(fname)
