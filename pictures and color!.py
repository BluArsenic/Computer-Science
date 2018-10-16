from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx,imgy))

image.putpixel((0,0),(255))
image.putpixel((256,256),(255,0,0))
image.save("demo.gif", "GIF")