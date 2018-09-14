import math

#w = 35.74+0.6215t+(04275t - 35.75)v**0.16

t = float(input("t:"))
v = float(input("v:"))

if t > 50 or t < -50:
	w = print("'t' needs to be less than the absolute value of 50")
if v > 120 or v < 3:
	w = print("'v' needs to be less than 20 and greater than 3")
else:
	w = 35.74 + (0.6215*t) + ((0.4275*t - 35.75)*v**0.16)
	print("Wind Chill:",w)