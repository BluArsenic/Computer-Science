from PIL import Image


def checkers():
	r = 0
	total = 255
	for i in range(imgx):
		if i%checksize == 0:
			r = total-r
		for j in range(imgy):
			if j%checksize == 0:
				r = total-r
			image.putpixel((i,j),(r,0,0))

checknumber = 16
checksize = 32
imgx = checksize*checknumber
imgy = imgx

image = Image.new("RGB",(imgx,imgy))

checkers()

image.save("checkers.png", "PNG")
