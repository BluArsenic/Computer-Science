#Guess The Song
p = 0

#BIG BANK
print("She said 'Whatchu' gon do if I leave?'")
song = input("What is this song?")
if song == "big bank" or "Big Bank" or "BIG BANK":
	print("Correct!")
	p=p+1
	print("Points:"+str(p))
else:
	print("Wrong!")