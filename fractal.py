#Dominic T.
#Oct. 19, 2018
#It creates three pictures, the first two a variation of the mandelbrot set,
#The third, a variation of the julia set
#On my honor, I have neither given, nor recieved unauthorized aid


from PIL import Image
import random
import math

imgx, imgy = 1024,1024
maxIt = 256

#xm = xmin, xx = xmax, ym = ymin, yy = ymax
def mandel(xm, xx, ym, yy):
	for x in range(imgx):
		cx = x*(xx-xm)/(imgx-1)+xm
		for y in range(imgy):
			cy = y*(yy-ym)/(imgy-1)+ym
			c = complex(cx,cy)
			z = 0
			for i in range(maxIt):
				if abs(z) > 2.0:
					break
				z = z**2 + c			
			r = 5*i
			g = (i*256)%24
			b = 256-i
			image.putpixel((x,y),(r,g,b))

#1st Image
xmin, xmax = random.uniform(-.665545120934758,-.4435235120934758), random.uniform(-.66554567,-.4435235432)
ymin, ymax = xmin, xmax
image = Image.new("RGB",(imgx,imgy))
mandel(xmin, xmax, ymin, ymax)
image.show("M Fractal 1.png","PNG")

#2nd Image
xmin, xmax = random.uniform(-.665545120934758,-.4435235120934758), random.uniform(-.66554567,-.4435235432)
ymin, ymax = xmin, xmax
image = Image.new("RGB",(imgx,imgy))
mandel(xmin, xmax, ymin, ymax)
image.show("M Fractal 2.png","PNG")
			
#xm = xmin, xx = xmax, ym = ymin, yy = ymax
def julia(xm, xx, ym, yy):
	cx = random.uniform(-.665545120934758,-.4435235120934758)
	cy = random.uniform(-.665545120934758,-.4435235120934758)
	c = complex(cx,cy)
	for x in range(imgx):
		zx = x*(xx-xm)/(imgx-1)+xm
		for y in range(imgy):
			zy = y*(yy-ym)/(imgy-1)+ym
			z = complex(zx,zy)
			for i in range(maxIt):
				if abs(z) > 2.0:
					break
				z = z**2 + c			
			r = 0
			g = (i*256)%24
			b = 256-i
			image.putpixel((x,y),(r,g,b))

#3rd Image
xmin, xmax = -1.0, 1.0
ymin, ymax = xmin, xmax
image = Image.new("RGB",(imgx,imgy))
julia(xmin, xmax, ymin, ymax)
image.show("M Fractal 3.png","PNG")