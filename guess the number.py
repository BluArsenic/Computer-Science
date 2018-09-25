import random

y = float(input("Highest guessing number:"))
x = random.randint(1, y)

def guess():
	number = input("Guess the number I'm thinking of between 1 and",y)

guess()