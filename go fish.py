import random

class Deck:
	# creates the game deck and the player's decks/hands
	def __init__(self):
		self.deck = []
		self.playerDeck = []
		self.enemyDeck = []
		self.playerMatch = []
		self.opponentMatch = []
		self.newoppHand = []
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
		# calls the shuffle function
		self.shuffle()

	# shuffles the deck
	def shuffle(self):
		random.shuffle(self.deck)

	# takes the top 7 cards of the deck and adds them to the player's hand 
	def playerAdd(self):
		status = ""
		for x in range(7):
			self.playerDeck.append(self.deck.pop(x))
			status += "\n"+str(self.playerDeck[x][0])+" of "+str(self.playerDeck[x][1])
		status = "\nYour Cards:"+status
		return status

	# takes the next top 7 cards of the deck and adds them to the opponent's hand 
	def opponentAdd(self):
		status = ""
		for x in range(8,15):
			self.enemyDeck.append(self.deck.pop(x))
		status += "\nYour oppenent has "+str(len(self.enemyDeck))+" cards."
		return status

	# displays the player's hand
	def playerHand(self):
		status = ""
		for x in range(len(self.playerDeck)):
			status += "\n"+str(self.playerDeck[x][0])+" of "+str(self.playerDeck[x][1])
		status = "\nYour Cards:" + status
		return status

	#displays the amount of cards in the opponent's hand
	def opponentHand(self):
		status = ""
		for x in range(len(self.enemyDeck)):
			status += "\n"+str(self.enemyDeck[x][0])+" of "+str(self.enemyDeck[x][1])
		status = "\nYour Cards:"+status
		# status += "\nYour oppenent has "+str(len(self.enemyDeck))+" cards."
		return status

	#checks if the inputted card positions match; if they do, they get added to the "matches" (the matches list)
	def match(self, x, y):
		status = ""
		matches = ""
		if self.playerDeck[x][0] != self.playerDeck[y][0]:
			print("This is not a match.")
		elif self.playerDeck[x][0] == self.playerDeck[y][0]:
			self.playerMatch.append(self.playerDeck.pop(x))
			self.playerMatch.append(self.playerDeck.pop(y-1))
		for x in range(len(self.playerDeck)):
			status += "\n"+str(self.playerDeck[x][0])+" of "+str(self.playerDeck[x][1])
		status = "\nYour Cards:"+status
		for x in range(len(self.playerMatch)):
			matches += "\n"+str(self.playerMatch[x][0])+" of "+str(self.playerMatch[x][1])
		matches = "\nYou have "+str(len(self.playerMatch)/2)+" matches.\n\nYour Matches:" + matches
		print(matches)
		return status

	def oppMatch(self):
		status = ""
		matches = ""
		for x in range(len(self.enemyDeck)):
			for y in range(len(self.enemyDeck)):
				if self.enemyDeck[x][0] == self.enemyDeck[y][0] and self.enemyDeck[x][1] != self.enemyDeck[y][1]:
					self.opponentMatch.append(self.enemyDeck[x])
					self.opponentMatch.append(self.enemyDeck[y])
					del self.opponentMatch[-1]
		for x in range(len(self.opponentMatch)):
			for y in range(len(self.enemyDeck)):
				if self.opponentMatch[x][0] == self.enemyDeck[y][0] and self.opponentMatch[x][1] != self.enemyDeck[y][1]:
					self.newoppHand += self.enemyDeck.pop(y)
					self.enemyDeck.append(self.newoppHand)
		if len(self.opponentMatch) > 0:
			temp = len(self.opponentMatch)
			del self.enemyDeck[0-temp:]
			self.newoppHand = []
		# for x in range(len(self.enemyDeck)):
		# 	status += "\n"+str(self.enemyDeck[x][0])+" of "+str(self.enemyDeck[x][1])
		# status = "\nYour Cards:"+status
		status += "\nYour oppenent has "+str(len(self.enemyDeck))+" cards."
		# for x in range(len(self.opponentMatch)):
		# 	matches += "\n"+str(self.opponentMatch[x][0])+" of "+str(self.opponentMatch[x][1])
		matches = "\nYour oppenent has "+str(len(self.opponentMatch)/2)+" matches."
		print(matches)
		return status

	def mechanics(self):
		ask = int(input("\nSelect the position (a number) you want to ask for: "))
		for y in range(len(self.enemyDeck)):
			if self.enemyDeck[y][0] != self.playerDeck[ask][0]:
				print("Go fish!")
				self.playerDeck.append(self.deck.pop(0))
				self.oppMechanics()
			elif self.enemyDeck[y][0] == self.playerDeck[ask][0]:
				self.playerDeck.append(self.enemyDeck[y])
				self.newoppHand += self.enemyDeck.pop(y)
				self.enemyDeck.append(self.newoppHand)
		if len(self.newoppHand) > 0:
			temp = len(self.newoppHand)
			del self.enemyDeck[-temp:]
			self.newoppHand = []

	def oppMechanics(self):
		ask = int(input("\nSelect the position (a number) you want to ask for: "))
		for x in range(len(self.playerDeck)):
			if self.playerDeck[y][0] != self.enemyDeck[random.randint(len(self.enemyDeck))][0]:
				print("Go fish!")
				self.enemyDeck.append(self.deck.pop(0))
				self.mechanics()
			elif self.playerDeck[y][0] == self.enemyDeck[random.randint(len(self.enemyDeck))][0]:
				self.enemyDeck.append(self.playerDeck[y])
				self.newoppHand += self.playerDeck.pop(y)
				self.playerDeck.append(self.newoppHand)
		if len(self.newoppHand) > 0:
			temp = len(self.newoppHand)
			del self.playerDeck[-temp:]
			self.newoppHand = []


playerDeck = Deck()
enemyDeck = Deck()
true = True
# prints the addition of the cards in the hand
print(playerDeck.playerAdd())
print(enemyDeck.opponentAdd())
while true:
	# asks if there are matching cards; this means it's up to the player to determine if hey have a match or not
	askMatch = input("\nAre there any matching cards? Y or N: ")
	# changes the answer to a lowercase answer
	askMatch = askMatch.lower()
	if askMatch == "y" or askMatch == "yes":
		inputOne = int(input("\nEnter the position of the first matching card: "))-1
		inputTwo = int(input("\nEnter the position of the second matching card: "))-1
		print(playerDeck.match(inputOne, inputTwo))
		print(enemyDeck.oppMatch())
	else:
		true = False
		print(playerDeck.playerHand())
		print(enemyDeck.oppMatch())

print(playerDeck.mechanics())
print(enemyDeck.oppMechanics())