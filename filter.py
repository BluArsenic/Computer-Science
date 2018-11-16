from PIL import Image, ImageDraw
import random

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

imgx = 178
img = Image.new("RGB", (imgx, imgx))

for x in range(imgx):
	for y in range(imgx):
		img.putpixel((x,y),(r,g,b))

img.save("color.png", "PNG")

picture = Image.open("color.png")
image = Image.open("doggo.jpeg")

Image.blend(image, picture, .5).show("test.png", "PNG")
