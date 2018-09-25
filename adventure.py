def start():
	choice = input("\n\n\n\n\n\nGreetings! \n\nYou are heading to the dining hall one day"
	    "when there's a bear walking with a dinosaur on campus!! Do you"
	    "\n\n1) Run, 2) Hide, or 3) Resist? \n\n>>")
	    #/n = enter \s = space \t = tab
	if choice == "1":
		inside()
	elif choice == "2":
		inside()
	elif choice == "3":
		walkWithDinoBear()
	else:
		print("You nincompoop!")
		exit()

def inside():
	print("Lame!")

def walkWithDinoBear():
	print("We love a brave sister")

start()
# exit() >> ends the game