#!/usr/bin/env python3

from PIL import Image

im = Image.open('/home/amurillo/pruebas/001.tiff')
im.convert('RGB').resize((600, 400)).save('/home/amurillo/pruebas/001.jpeg')
