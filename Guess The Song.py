#Dominic Thomas
#9-21-18
#Guess The Song
#I wasn't able to keep guessSong() because it wouldn't update the point system
#On my honor, I have neither given nor recieved unauthorized aid

import random

r = random.randint(1,30)
p = 0 #points
c = 0 #song count

def exit():
	global quit
	quit = input("Quit (q) or Continue (c)? ")
	quit = quit.lower
	if quit is "q": # or quit is "quit":
		quit()
	elif quit is "c": # or quit is "continue":
		return
	# else:
	# 	while True:
	# 		try:
	# 			quit = input("Quit (q) or Continue (c)? ")
	# 			break
	# 		except ValueError:
	# 			print("Please enter 'q' or 'c': ")

def guessSong(x):
	global p
	global c
	song = input("What is this song?")
	song = song.lower()
	if song == str(x):
		print("Correct!")
		p=p+1
		c+=1
	else:
		print("Wrong!")
		p=p-1
		c+=1

def opening():
	print("\n\nHello! Welcome to my game! In this game, you will be guessing 30 different songs."
		"\nHere are the rules:"
		"\n\n1) You currently get one try at guessing the song"
		"\n2) No punctuation or capitilization is required"
		"\n3) You have to type in the entire name of the song; some songs have one exception"
		"\n4) If you get guess correctly, you get one point; if you don't you lose one point"
		"\n5) Guess as many songs as you can and have fun!")

opening()

#Let it Go
print("\n\nI don't care what they're going to say")
guessSong("let it go")
exit()

#Me & You
print("\n\nDid you really mean the words that you said?")
guessSong("me and you")

#Do You Want To Build A Snowman
print("\n\nWe used to be best buddies, and now we're not, I wish you would tell me why")
guessSong("do you want to build a snowman" or "build a snowman")

#High School Musical
print("\n\nIt's the best part we've ever known, step into the future")
guessSong("high school musical")

#A Whole New World
print("\n\nA dazzling place I never knew")
guessSong("a whole new world" or "whole new world")

#Reflection
print("\n\nWho is that girl I see staring straight back at me?")
guessSong("reflection")

#Just Can't Wait To Be King
print("\n\nLet's hear it in the herd and on the wing")
guessSong("just cant wait to be king" or "i just cant wait to be king")

#How Far I'll Go
print("\n\nAnd no one knows, hw far it goes")
guessSong("how far ill go")

#I'll Make A Man Out Of You
print("\n\nMysterious as the dark side of the moon")
guessSong("ill make a man out of you")

#Hakuna Matata
print("\n\nIt means no worries for he rest of your days")
guessSong("hakuna matata" or "no worries")

#BIG BANK
print("\n\nShe said 'Whatchu' gon do if I leave?'")
guessSong("big bank")

#Owe Me
print("\n\nThe smile on your face the only thing I can't read")
guessSong("owe me")

#This Feeling
print("\n\nThey tell me think with your head, not that thing in my chest")
guessSong("this feeling")
	
#This is America
print("\n\nDon't catch you slippin' now")
guessSong("this is america")

#1 Thot, 2 Thot
print("\n\nGot your girl in the kitchen cooking up some pork chops")
guessSong("1 thot 2 thot")

#Yosemite
print("\n\nShine like the sun, you truly blessed")
guessSong("yosemite")

#Homemade Dynamite
print("\n\nI'll give you my best side, tell you all my best lies")
guessSong("homemade dynamite")

#K.O.D
print("\n\nThis is what you call a flip, ten keys from a quarter brick")
guessSong("kod")

#You're Welcome
print("\n\nI killed an eel, I buried its guts, sprouted a tree, now you've got coconuts")
guessSong("youre welcome")

#2009
print("\n\nOh, no, I take it if it's mine, I don't stay inside the lines")
guessSong("2009")

#Natural
print("\n\nLiving your life cutthroat, you gotta be so cold")
guessSong("natural")

#Everytime We Touch
print("\n\nCan't you feel my heart beat fast, I want this to last")
guessSong("everytime we touch")

#Waka Waka
print("\n\nTsamina mina zangalewa, anawa a a")
guessSong("waka waka")

#Crazy in Love
print("\n\nGot me hoping you page me right now, your kiss got me hoping you save me right now")
guessSong("crazy in love")

#American Idiot
print("\n\nWelcome to a new kind of tension all across the alien nation")
guessSong("american idiot")

#Party Rock
print("\n\nAnd we gon' make you lose your mind, everybody just have a good time")
guessSong("party rock")

#She Will Be Loved
print("\n\nI don't mind spending every day out on your corner in the pouring rain")
guessSong("she will be loved")

#Dynamite
print("\n\nI throw my hands up in the air sometimes saying 'Ayo! Gotta let go!'")
guessSong("dynamite")

#You Belong With Me
print("\n\nIf you could see that I'm the one who understands you, been here all along, so why can't you see?")
guessSong("you belong with me")

#Tik Tok
print("\n\nDon't stop, make it pop, DJ, blow my speakers up")
guessSong("tik tok" or "tick tock")

#Live Your Life
print("\n\nYou're gonna be, a shinin' star, in fancy clothes, and fancy cars")
guessSong("live your life")

print("Congratulations! You made it through the game! Here's your score:")
print(p)