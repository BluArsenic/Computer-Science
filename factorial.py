def fact(n):
	if n is 1:
		return 1
	return n*fact(n-1)

number = int(input("N:"))
fact(number)
print(fact(number))