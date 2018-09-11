import random
a = random.randint(1,4)

print("Hello!")
if a == 1:
	print("1. Good  2. Not so great  3. OK  4. Great!")
	a1 = input("How are you?")
elif a == 2:
	print("1. Good  2. Not so great  3. OK  4. Great!")
	a2 = input("How was your day so far?")
elif a == 3:
	print("1. Good  2. Not so great  3. OK  4. Great!")
	a3 = input("How was your weekend?")
elif a == 4:
	print("1. Yes  2. No")
	a4 = input("Were you busy this week?")

#help from https://www.youtube.com/watch?v=BuHdv0rkO_k
#i.e. a1 = "1"

#FIRST QUESTION (How are you?)>>>>>

#first branch from first main question
if a == 1 and a1 == "1":
	print("1. Going to class  2. I'm in class  3. Chillin'  4. Going to my room")
	b1 = input("What are you doing now?")
	#done done done done done
elif a == 1 and a1 == "2":
	b1 = print("I'm sorry to hear. I hope it gets better!")
	#done done done done done
elif a == 1 and a1 == "3":
	print("1. I went to class  2. I went to my room  3. I went to the SAC  4. Nothing, really  5. *something productive*")
	b1 = input("Well, what did you do today?")\
	#done done done done done
elif a == 1 and a1 == "4":
	print("1. Class  2. St. John  3. My room  4. *somewhere productive*")
	b1 = input("Good to hear! Where are you going now?")
	#done done done done done

#first branch from first side question
if a == 1 and a1 == "1" and b1 == "1":
	print("1. Yes  2.No")
	c1 = input("Do we have the same class?")
elif a == 1 and a1 == "1" and b1 == "2":
	print("Oh. Sorry to bother you. Have fun in class!")
elif a == 1  and a1 == "1" and b1 == "3":
	print("Alright. Have fun!")
elif a == 1 and a1 == "1" and b1 == "4":
	print("Oh, ok. Have fun then!")

#second branch of first side question
if a == 1 and a1 == "1" and b1 == "1" and c1 == "1":
	print("Ok, cool. Let's walk to class together.")
elif a == 1 and a1 == "1" and b1 == "1" and c1 == "2":
	print("Ok. See ya later!")

#first branch of third side question
if a == 1 and a1 == "3" and b1 == "1":
	print("1. Boring  2. Fun, actually  3. Alright")
	c1 = input("How was it?")
elif a == 1 and a1 == "3" and b1 == "2":
	print("1. Nothing  2. Work  3. Sleep")
	c1 = input("What did you do?")
elif a == 1 and a1 == "3" and b1 == "3":
	print("1. Nothing  2. Work  3. Sleep  4. Play games")
	c1 = input("What did you do?")
elif a == 1 and a1 == "3" and b1 == "4":
	print("Oh, ok.")
elif a == 1 and a1 == "3" and b1 == "5":
	print("Good for you!")

#second branch of third side question
if a == 1 and a1 == "3" and b1 == "1" and c1 == "1":
	print("Aw, that stinks.")
elif a == 1 and a1 == "3" and b1 == "1" and c1 == "2":
	print("That's nice.")
elif a == 1 and a1 == "3" and b1 == "1" and c1 == "3":
	print("That's cool.")

#third branch of third side quesiton
if a == 1 and a1 == "3" and b1 == "2" and c1 == "1":
	print("Same.")
elif a == 1 and a1 == "3" and b1 == "2" and c1 == "2":
	print("Nice!")
elif a == 1 and a1 == "3" and b1 == "2" and c1 == "3":
	print("Same.")

#fourth branch of third side question
if a == 1 and a1 == "3" and b1 == "3" and c1 == "1":
	print("Same.")
elif a == 1 and a1 == "3" and b1 == "3" and c1 == "2":
	print("Nice!")
elif a == 1 and a1 == "3" and b1 == "3" and c1 == "3":
	print("Same.")
elif a == 1 and a1 == "3" and b1 == "3" and c1 == "4":
	print("Same.")

#first branch of fourth side question
if a == 1 and a1 == "4" and b1 == "1":
	print("Have fun!")
elif a == 1 and a1 == "4" and b1 == "2":
	print("Have fun!")
elif a == 1 and a1 == "4" and b1 == "3":
	print("Have fun!")
elif a == 1 and a1 == "4" and b1 == "4":
	print("Good luck!")



#SECOND QUESTION (How was your day so far?)>>>>>>>

#first branch from second main question
if a == 2 and a2 == "1":
	print("1. Going to class  2. I'm in class  3. Chillin'  4. Going to my room")
	b2 = input("What are you doing now?")
	#done done done done done
elif a == 2 and a2 == "2":
	b2 = print("I'm sorry to hear. I hope it gets better!")
	#done done done done done
elif a == 2 and a2 == "3":
	print("1. I went to class  2. I went to my room  3. I went to the SAC  4. Nothing, really  5. *something productive*")
	b2 = input("Well, what did you do today?")
elif a == 2 and a2 == "4":
	print("1. Class  2. St. John  3. My room  4. *somewhere productive*")
	b2 = input("Good to hear! Where are you going now?")

#first branch of second side question
if a == 2 and a2 == "1" and b2 == "1":
	print("1. Yes  2.No")
	c2 = input("Do we have the same class?")
elif a == 2 and a2 == "1" and b2 == "2":
	print("Oh. Sorry to bother you. Have fun in class!")
elif a == 2  and a2 == "1" and b2 == "3":
	print("Alright. Have fun!")
elif a == 2 and a2 == "1" and ab == "4":
	print("Oh, ok. Have fun then!")

#second branch of second question
if a == 2 and a2 == "1" and b2 == "1" and c2 == "1":
	print("Ok, cool. Let's walk to class together.")
elif a == 2 and a2 == "1" and b2 == "1" and c2 == "2":
	print("Ok. See ya later!")

#first branch of third side question
if a == 2 and a2 == "3" and b2 == "1":
	print("1. Boring  2. Fun, actually  3. Alright")
	c2 = input("How was it?")
elif a == 2 and a2 == "3" and b2 == "2":
	print("1. Nothing  2. Work  3. Sleep")
	c2 = input("What did you do?")
elif a == 2 and a2 == "3" and b2 == "3":
	print("1. Nothing  2. Work  3. Sleep  4. Play games")
	c2 = input("What did you do?")
elif a == 2 and a2 == "3" and b2 == "4":
	print("Oh, ok.")
elif a == 2 and a2 == "3" and b2 == "5":
	print("Good for you!")

#second branch of third side question
if a == 2 and a2 == "3" and b2 == "1" and c2 == "1":
	print("Aw, that stinks.")
elif a == 2 and a2 == "3" and b2 == "1" and c2 == "2":
	print("That's nice.")
elif a == 2 and a2 == "3" and b2 == "1" and c2 == "3":
	print("That's cool.")

#third branch of third side quesiton
if a == 2 and a2 == "3" and b2 == "2" and c2 == "1":
	print("Same.")
elif a == 2 and a2 == "3" and b2 == "2" and c2 == "2":
	print("Nice!")
elif a == 2 and a2 == "3" and b2 == "2" and c2 == "3":
	print("Same.")

#fourth branch of third side question
if a == 2 and a2 == "3" and b2 == "3" and c2 == "1":
	print("Same.")
elif a == 2 and a2 == "3" and b2 == "3" and c2 == "2":
	print("Nice!")
elif a == 2 and a2 == "3" and b2 == "3" and c2 == "3":
	print("Same.")
elif a == 2 and a2 == "3" and b2 == "3" and c2 == "4":
	print("Same.")

#first branch of fourth side question
if a == 2 and a2 == "4" and b2 == "1":
	print("Have fun!")
elif a == 2 and a2 == "4" and b2 == "2":
	print("Have fun!")
elif a == 2 and a2 == "4" and b2 == "3":
	print("Have fun!")
elif a == 2 and a2 == "4" and b2 == "4":
	print("Good luck!")



#THIRD QUESTION (How was your weekend?)>>>>>>>>

#first branch of third question
if a == 3 and a3 == "1":
	print("1. Going to class  2. I'm in class  3. Chillin'  4. Going to my room")
	b3 = input("What are you doing now?")
	#done done done done done
elif a == 3 and a3 == "2":
	b3 = print("I'm sorry to hear. I hope it gets better!")
	#done done done done done
elif a == 3 and a3 == "3":
	print("1. I went to class  2. I went to my room  3. I went to the SAC  4. Nothing, really  5. *something productive*")
	b3 = input("Well, what did you do today?")
elif a == 3 and a3 == "4":
	print("1. Class  2. St. John  3. My room  4. *somewhere productive*")
	b3 = input("Good to hear! Where are you going now?")

#second branch of first question
if a == 3 and a3 == "1" and b3 == "1":
	print("1. Yes  2.No")
	c3 = input("Do we have the same class?")
elif a == 3 and a3 == "1" and b3 == "2":
	print("Oh. Sorry to bother you. Have fun in class!")
elif a == 3  and a3 == "1" and b3 == "3":
	print("Alright. Have fun!")
elif a == 3 and a3 == "1" and b3 == "4":
	print("Oh, ok. Have fun then!")

#third branch of first question
if a == 3 and a3 == "1" and b3 == "1" and c3 == "1":
	print("Ok, cool. Let's walk to class together.")
elif a == 3 and a3 == "1" and b3 == "1" and c3 == "2":
	print("Ok. See ya later!")

#first branch of third side question
if a == 3 and a3 == "3" and b3 == "1":
	print("1. Boring  2. Fun, actually  3. Alright")
	c2 = input("How was it?")
elif a == 3 and a3 == "3" and b3 == "2":
	print("1. Nothing  2. Work  3. Sleep")
	c2 = input("What did you do?")
elif a == 3 and a3 == "3" and b3 == "3":
	print("1. Nothing  2. Work  3. Sleep  4. Play games")
	c2 = input("What did you do?")
elif a == 3 and a3 == "3" and b3 == "4":
	print("Oh, ok.")
elif a == 3 and a3 == "3" and b3 == "5":
	print("Good for you!")

#second branch of third side question
if a == 3 and a3 == "3" and b3 == "1" and c3 == "1":
	print("Aw, that stinks.")
elif a == 3 and a3 == "3" and b3 == "1" and c3 == "2":
	print("That's nice.")
elif a == 3 and a3 == "3" and b3 == "1" and c3 == "3":
	print("That's cool.")

#third branch of third side quesiton
if a == 3 and a3 == "3" and b3 == "2" and c3 == "1":
	print("Same.")
elif a == 3 and a3 == "3" and b3 == "2" and c3 == "2":
	print("Nice!")
elif a == 3 and a3 == "3" and b3 == "2" and c3 == "3":
	print("Same.")

#fourth branch of third side question
if a == 3 and a3 == "3" and b3 == "3" and c3 == "1":
	print("Same.")
elif a == 3 and a3 == "3" and b3 == "3" and c3 == "2":
	print("Nice!")
elif a == 3 and a3 == "3" and b3 == "3" and c3 == "3":
	print("Same.")
elif a == 3 and a3 == "3" and b3 == "3" and c3 == "4":
	print("Same.")


#first branch of fourth side question
if a == 3 and a3 == "4" and b3 == "1":
	print("Have fun!")
elif a == 3 and a3 == "4" and b3 == "2":
	print("Have fun!")
elif a == 3 and a3 == "4" and b3 == "3":
	print("Have fun!")
elif a == 3 and a3 == "4" and b3 == "4":
	print("Good luck!")



#FOURTH QUESTION (Were you busy this week?)>>>>>>>>>>

#first branch from forth main question
if a == 4 and a4 == "1":
	print("1. A lot  2. 4 hours  3. Only one assignment, but a hard long one")
	b4 = input("How much work did you have?")
elif a == 4 and a4 == "2":
	print("Oh, that's sweet!")

#first branch from first side question
if a == 4 and a4 == "1" and b4 == "1":
	print("Oooh, that's rough!")
elif a == 4 and a4 == "1" and b4 == "2":
	print("Oooh, that's rough!")
elif a == 4 and a4 == "1" and b4 == "3":
	print("Oooh, that's rough!")