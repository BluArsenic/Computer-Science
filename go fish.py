class Deck:
	def __init__(self):
		self.deck = []
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
				self.deck.append((i,j))
		self.shuffle()

	def shuffle(self):
		random.shuffle(self.deck)	

	def __str__(self):
		status = ""		
		for x in range(len(self.deck)):
			status += "\n"+str(self.deck[x][0])+" of "+str(self.deck[x][1])
		return status