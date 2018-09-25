while True:
	try:
		x = int(input("Enter a number: "))
		break
	except ValueError:
		print("wrong my guy")

count = 0

while count < x:
	print("Hello!")
	count+=1

