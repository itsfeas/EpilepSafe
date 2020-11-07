from PIL import Image
from random import randrange
import cv2

im = Image.open('Dino.png') # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
for x in range(1,100):
	print(pix[x,x])  # Get the RGBA Value of the a pixel of an image
	pix[x,x] = (0,255,0)
	pix[x+1,x] = (0,255,0)
	pix[x+2,x] = (0,255,0)
	pix[x+3,x] = (0,255,0)

for x in range(100,600):
	print(pix[100,x])
	pix[100,x] = (0,255,0)  # Set the RGBA Value of the image (tuple)

for x in range(100,600):
	print(pix[100,x])  # Get the RGBA Value of the a pixel of an image
	pix[100,x] = (0,255,0)  # Set the RGBA Value of the image (tuple)

for x in range(100,600):
	pix[x,600] = (0,255,0)  # Set the RGBA Value of the image (tuple)
	pix[x+1,600] = (0,255,0)  # Set the RGBA Value of the image (tuple)
	pix[x+2,600] = (0,255,0)  # Set the RGBA Value of the image (tuple)
	pix[x+3,600] = (0,255,0)  # Set the RGBA Value of the image (tuple)

for x in range(5000):
	a = randrange(1040)
	b = randrange(709)
	pix[a, b] = (0,255,0)
	pix[a+1, b+1] = (0,255,0)
	pix[a, b+1] = (0,255,0)
	pix[a+1, b] = (0,255,0)

im.save('alive_parrot.png')  # Save the modified pixels as .png
