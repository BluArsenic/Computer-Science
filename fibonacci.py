a = int(input("Number:"))

def fibo(n):
	if n == 0:
		print("Fibo Number: 0")
	elif n == 1:
		print("Fibo Number: 1")
	elif n > 1:
		n = (n-1) + (n-2)
		print("Fibo Number:",n)
	else:
		print("incorrect")

fibo(a)