from PIL import Image, ImageDraw

imgx = 256
image = Image.new('RGBA',(imgx,imgx), (255))

for x in range(imgx):
	for y in range(imgx):
		image.putpixel((x,y),(0,255,0,0))

Image.blend(image, image, .3).show("test.png", "PNG")