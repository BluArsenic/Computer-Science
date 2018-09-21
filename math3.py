import math
import sys

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])
yy = int(y - (14 - m)/12)
x = int(yy + (yy/4) - (yy/100) + (yy/400))
mm = int(m +12 * ((14 - m)/12)-2)
dd = int((d + x + (31*mm)/12)%7%7)

if 1 > m > 12:
	print("Enter a number that corresponds with a month (Jan. = 1, Feb. = 2, etc.)")
elif 1 > d > 31:
	print("Enter a a valid number")
else:
	yy
	x
	mm
	print("Day:",dd)

#y0  =  y  -  (14  -  m)  /  12  
#x  =  y0  +  y0/4  -  y0/100  +  y0/400  
#m0  =  m  +  12  *  ((14  -  m)  /  12)  -  2  
#d0  =  (d  +  x  +  (31*m0)/  12)  mod  7