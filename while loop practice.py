def question():
	response = input("Give me info: ")
	while response != "hi" or "b":
		print("This is useless info! Try again.")
		response = input("Give me info: ")
	if response == "hi":
		print("a")
	elif response == "b":
		print("b")

question()