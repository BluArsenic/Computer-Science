class Dog:
	#constructor
	#initializes properties and sets up the dog object
	#kind = "Dog"
	def __init__(self, name, hunger, energy):
		self.name = name
		self.hunger = hunger
		self.energy = energy

	#methods/functions
	def eat(self):
		status = ""
		if self.hunger > 0:
			self.hunger -= 1
			self.energy += 1
			status = self.name+" just ate a delicious meal!"
		else:
			status = self.name+" is not hungry!"
		return status		

	def stats(self):
		return "Name: "+self.name+"\nEnergy: "+str(self.energy)+"\nHunger: "+str(self.hunger)

dogName = input("What do you want to name your dog?")
dog1 = Dog(dogName, 5, 2)
dog2 = Dog("Mary", 3, 9)

while True:
	print(dog1.stats())
	print(dog2.stats())
	choice = input("What do you want to do?")
	if choice == "eat":
		print(dog1.eat())
		print(dog2.eat())
	else:
		print("Can't do that!")