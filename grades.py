g = float(input("Grade:"))

if g > 4.85:
	print("A+")
elif 4.85 > g > 4.7:
	print("A")
elif 4.7 > g > 4.5:
	print("A-")
elif 4.5 > g > 4.2:
	print("B+")
elif 4.2 > g > 3.85:
	print("B")
elif 3.85 > g > 3.5:
	print("B-")
elif 3.5 > g > 3.2:
	print("C+")
elif 3.2 > g > 2.85:
	print("C")
elif 2.85 > g > 2.5:
	print("C-")
elif 2.5 > g > 2:
	print("D+")
elif 2 > g > 1.5:
	print("D")
elif 1.5 > g > 1:
	print("D-")
elif 1 > g > 0:
	print("F")
elif 0 > g > 5:
	print("Please enter a number between 0 and 5")