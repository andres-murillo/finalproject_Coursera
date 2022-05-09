#!/usr/bin/env python3

from sys import orig_argv
from PIL import Image
import os

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = image.open(f)
        fname, ext = os.path.splitext(f)
        print(fname)
