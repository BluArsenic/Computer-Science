from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx,imgy))

def color(x, y):
	for i in range(x,y,32):
		for j in range(0,imgx):
			image.putpixel((i,j),(255))
			image.putpixel((imgx-1,j),(255))
	for k in range(0,imgy):
		for l in range(x,y,32):
			image.putpixel((k,l),(255))
			image.putpixel((k,imgy-1),(255))

color(0, 512)
image.save("rainbow.png", "PNG")
