class Bank:
	def __init__(self, name, dep, wit, acc): #you don't have to use all the variables
		bal = 200
		self.balance = bal
		self.deposit = dep
		self.name = name
		self.withdraw = wit
		self.accounts = acc
		self.user = 50

	def withdrawal(self, take):
		status = ""
		if take > self.balance:
			status = "\nYou can't withdraw more than you have."
		elif self.balance > 0:
			self.balance -= take
			self.user += take
			status = "\nYou just took $"+str(take)+" out of your account."
		else:
			status = "\nYou can't overdraw your account!"
		return status

	def stats(self):
		return "\nName: "+self.name+"\nBalance: $"+str(self.balance)+"\nIn-Pocket: $"+str(self.user)

bankName = input("What is your name?")
create = input("Would you like to create a bank account? (Y) or (N)?")
if create == "y":
	bank1 = Bank(bankName, 0, 0, 0)
else:
	quit()

print(bank1.stats())

def withdraw():
	takeOut = int(input("\nHow much money would you like to withdraw?"))
	print(bank1.withdrawal(takeOut))
	print(bank1.stats())

choice = input("\nWhat would you like to do?\n Deposit? (D)\n Withdraw? (W)\n Transfer? (T)\nChoice?: ")
if choice == "w":
	withdraw()
