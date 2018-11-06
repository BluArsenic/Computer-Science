import random

class Card:
	def __init__(self):
		self.deck = []	
	def __str__(self):
		card = self.deck
		status = ""
		for i in range(1,14):
			for j in range(1,5):
				if i is 1:
					i = "Ace"
				elif i is 11:
					i = "Jack"
				elif i is 12:
					i = "Queen"
				elif i is 13:
					i = "King"
				if j is 1:
					j = "Clubs"
				elif j is 2:
					j = "Diamonds"
				elif j is 3:
					j = "Hearts"
				elif j is 4:
					j = "Spades"
				card.append((i,j))
		x = random.randrange(len(card))
		status = "\n"+str(card[x][0])+" of "+str(card[x][1])
		return status		

class Deck:
	def __init__(self):
		self.deck = []	
	def __str__(self):
		deck = self.deck
		status = ""
		for i in range(1,14):
			for j in range(1,5):
				if i is 1:
					i = "Ace"
				elif i is 11:
					i = "Jack"
				elif i is 12:
					i = "Queen"
				elif i is 13:
					i = "King"
				if j is 1:
					j = "Clubs"
				elif j is 2:
					j = "Diamonds"
				elif j is 3:
					j = "Hearts"
				elif j is 4:
					j = "Spades"
				deck.append((i,j))
		random.shuffle(deck)	
		for x in range(len(deck)):
			status += "\n"+str(deck[x][0])+" of "+str(deck[x][1])
		return status
		# print(str(x[0])+" of "+str(x[1]))
		# print(str(i)+" of "+str(j))

print(Card())
print(Deck())