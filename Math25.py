import sys
import math

x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]

print(float(x), float(y), float(z))

if x > y > z:
	print("True")
elif x < y < z:
	print("True")
else:
	print("False")

#print("This is the name of the script: ", sys.argv[0])
#print("Number of arguments: ", len(sys.argv))
#print("The arguments are: " , str(sys.argv))