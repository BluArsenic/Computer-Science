class Bank:
	def __init__(self, name, bal, dep, wit, acc): #you don't have to use all the variables
		bal = 200
		self.balance = bal
		self.deposit = dep
		self.name = name
		self.withdraw = wit
		self.accounts = acc
		self.user = 50

	def withdrawal(self, take):
		status = ""
		if self.balance > 0:
			self.balance -= take
			status = "\nYou just took $"+str(take)+" out of your account."
		else:
			status = "\nYou can't overdraw your account!"
		return status

	def stats(self):
		return "\nName: "+self.name+"\nBalance: $"+str(self.balance)

bankName = input("What is your name?")
create = input("Would you like to create a bank account? (Y) or (N)?")
if create == "y":
	bank1 = Bank(bankName, 0, 0, 0, 0)
else:
	quit()

print(bank1.stats())

choiceWith = input("\nWould you like to withdraw from your account? (Y) or (N)?")
if choiceWith == "y":
	takeOut = int(input("How much money would you like to withdraw?"))
	print(bank1.withdrawal(takeOut))
	print(bank1.stats())
else:
	print(bank1.stats())
