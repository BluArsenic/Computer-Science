import math
import sys

e = math.exp(1)
P = float(sys.argv[1])
r = (float(sys.argv[2])/100)
t = float(sys.argv[3])

print(P*(e**(r*t)))