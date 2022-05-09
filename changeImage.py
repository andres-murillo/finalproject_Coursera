#!/usr/bin/env python3

from PIL import Image
import os

path = '/home/amurillo/pruebas/images/'
images = os.listdir(path)

for image in images:
	if image.endswith('tiff'):
		infile = path + image
		
		f, e = os.path.splitext(image)
		jpgfile = f + '.jpeg'
		outfile = path + jpgfile
		with Image.open(infile) as im:
			# outfile = im.convert('RGB')
			im.convert('RGB')
			im.save(outfile)




# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + '.jpg'
#     print(infile)
#     print(outfile)
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 # im.convert('RGB')
#                 im.save(outfile, 'JPEG')
#         except OSError as e:
#             print(e)
