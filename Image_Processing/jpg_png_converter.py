# jpg to png converter Script

import sys
import os

from PIL import Image

# Command: python jpg_png_converter.py input_folder/ output_folder/ 

image_folder = sys.argv[1]    # second parameter(input folder)
output_folder = sys.argv[2]   # third parameter(output folder)

if not os.path.exists(output_folder):
   os.makedirs(output_folder)

for filename in os.listdir(image_folder):
   img = Image.open(f'{image_folder}{filename}')   
   # split filename into clean name and extension
   clean_name = os.path.splitext(filename)[0]           
   extension = os.path.splitext(filename)[1]

   if (extension == '.jpeg' or extension =='.jpg'):
      img.save(f'{output_folder}{clean_name}.png', 'png')


