from PIL import Image

imgx = 256
image = Image.new("RGBA",(imgx,imgx))

for x in range(imgx):
	for y in range(imgx):
		image.putpixel((x,y),(255,0,0))

image.show("test.png", "PNG")