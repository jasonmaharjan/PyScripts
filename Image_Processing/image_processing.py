# Some Image Processing Scripts

from PIL import Image, ImageFilter

img = Image.open('./images/all.jfif')


# Blur Image
blur_image = img.filter(ImageFilter.BLUR)
blur_image.save('images/ blur.png', 'png')              # image.save('path/ filename', 'extension')


# Smooth Image
smooth_image = img.filter(ImageFilter.SMOOTH)
smooth_image.save('images/ smooth.png', 'png')


# Sharpen Image
sharpen_image = img.filter(ImageFilter.SHARPEN)
sharpen_image.save('images/ sharp.png', 'png')


# Grey Scale
greyscale_image = img.convert('L')
greyscale_image.save('images/ greyscale.png', 'png')


# Resize Image
resize_image = img.resize((300,200))        
resize_image.save('images/ resize.png', 'png')


# Rotate Image
rotate_image = img.rotate(180)
rotate_image.save('images/ rotate.png', 'png')


# Crop Image
box = (50,100,200,250)
crop_image = img.crop(box)
crop_image.save('images/ crop.png', 'png')


# Resize Images (With Aspect Ratio)!
img.thumbnail((400,200))
img.save('images/ resize_aspect.png','png')

