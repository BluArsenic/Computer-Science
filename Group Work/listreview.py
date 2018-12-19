import random as r

''' Instructions:
   Work with a partner to complete these tasks. You may assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''
faveNums = []
for i in range(3):
   faveNums.append(i)
print(faveNums)
 
''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays. 
'''
holidays = []
holidays.append("New Years")
holidays.append("Memorial")
holidays.append("Independence")
holidays.append("Christmas")
holidays.append("Thanksgiving")
holidays.append("Halloween")
holidays.append("Veterans")
holidays.append("Easter")
holidays.append("Columbus")
holidays.append("Presidents")
holidays.append("Labor")
holidays.append("Diwali")
holidays.append("Holi")
holidays.append("Cinco de Mayo")
holidays.append("Muharram")
print(holidays)
 
''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''
grades = []
for i in range(5):
   grades.append("A")
print(grades)
 
 
''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''
funny = []
for x in range(18):
   if x%2 == 0:
      x = True
      funny.append(x)
   else:
      x = False
      funny.append(x)
print(funny)
 
 
 
''' 5. 
   Create a list of floats, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''
import random as r
numEmployees = 100
salaries = []
for i in range(numEmployees):
   salaries.append(r.uniform(1.00,12567.88))
print(salaries)
 
''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''
grayscale = []
for j in range(x):
   for k in range(y):
      grayscale.append(image[x,y])
print(grayscale)
 
 
 
''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''
i = 0
students = []
students = [[0]*2 for x in range((noSiblings+oneSibling+TwoSibling+threeSibling))]
while noSiblings > 0 and oneSibling > 0 and twoSibling > 0 and threeSibling > 0:
   students[i][0] = "StudentName"
   students[i][1] = "StudentSibling"
   i += 1
print(students)

 
 
''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''
months = []
months.append("January")
months.append("Febuary")
months.append("March")
months.append("April")
months.append("May")
months.append("June")
months.append("July")
months.append("August")
months.append("September")
months.append("October")
months.append("November")
months.append("December")
print(months)

 
''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''
 week = []
 week.append("Monday")
 week.append("Tuesday")
 week.append("Wednesday")
 week.append("Thursday")
 week.append("Friday")
 week.append("Saturday")
 week.append("Sunday")
 print(week)

 
 
''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''
boolean = []
boolean.append(True)
boolean.append(False)
print(boolean)
 
 
''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''
 dorms = []
 dorms.append("Mem")
 dorms.append("Nichols")
dorms.append("Pitman")
dorms.append("Squire")
#etc.

''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
floats = []
for i in range(3):
   floats.append(r.uniform(0,1))
print(floats)


 
 
 
''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''
deck = [[0]*13 for x in range(4)]
 for i in range(4):
   if i == 0:
      suit = "D"
   if i == 1:
      suit = "C"
   if i == 2:
      suit = "H"
   if i == 3:
      suit = "S"
   for q in range(1,13):
      num = q
      if q == 1:
         num = "A"
      if q == 10:
         num = "J"
      if q == 11:
         num = "Q"
      if q == 12:
         num = "K"
      deck[i][q] = str(suit)+str(num)
   del deck[i][0]
for x in deck:
    print(*x)

 
''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''
yahtzee = []
import random as r
for i in range(5):
   dice = r.randint(1,6)
   yahtzee.append(dice)
   for j in range(5):
      if len(yahtzee) == 5:
         if yahtzee[0] == j:
            if yahtzee[1] == j:
               if yahtzee[2] == j:
                  if yahtzee[3] == j:
                     if yahtzee[4] == j:
                        print("Yahtzee!")
         elif yahtzee[i] != yahtzee[j]:
            print("Still checking...")
print(yahtzee)

 
 
''' 15. 
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''
a = [[0]*10 for x in range(10)]

for wide in range(10):
   for tall in range(10):
      check = a[tall][wide]
      if wide>0:
         check2 = a[tall][wide-1]
      else:
         check2 = a[tall-1][10]
      if wide < 9:
         check3 = a[tall][wide+1]
      else:
         check3 = a[tall+1][0]
      if check%3 == 0 and check2%2 == 0 and check3%2 == 1:
         print("Coordinates ("+str(wide)+",",str(tall)+"):")
      

 
 
''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''
import random as r
saddle = []
points = []
for x in range(5):
   saddle.append([r.randint(0,10) for x in range(5)])
for x in saddle:
   print(x)
for x in range(5):
   for y in range(5):
      if saddle[x][y] > saddle[x][y] and saddle[x][y] < saddle[x][y]:
         print("Coordinates: ("+str(x)+", "+str(y)+")")
         points.append((x,y))
if len(points) == 0:
   print("No saddle points. :)")
 
 
''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''
 
 
 
''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''
someList = []
for x in range(1,6):
   someList.append(x)
print(someList)
someList.reverse()
print(someList)
 
 
 
''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''
 
 
 
''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''
numbers = []
import random as r
for x in range(5):
   numbers.append(r.randint(0, 10))
for x in range(len(numbers)):
   for y in range(len(numbers)):
      if numbers[x] > numbers[y]:
         numbers.append(numbers.pop(x))
 
 
''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''
 
 
 
''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 55, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''
w = 5
h = 5
picture = []
import random as r
for x in range(w):
   picture.append([r.randint(0,255)]*w for x in range(h))
for x in picture:
   print(x)
for x in range(w):
   for y in range(h):
      picture[x][y] = -1*((picture[x][y])-255)
 
 
''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''
 
 
 
''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''
w = 5
h = 5
elevation = []
peak = []
import random as r
for x in range(w):
   elevation.append([r.randint(0,255)]*w for x in range(h))
for x in elevation:
   print(x)
if elevation[x][y] > elevation[x-1][y]:
   if elevation[x][y] > elevation[x][y-1]:
      if elevation[x][y] > elevation[x+1][y]:
         if elevation[x][y] > elevation[x][y+1]:
            peak.append(elevation[x][y])
print(peak)
 
''' 25. 
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''
 
 
 
''' 26. 
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''
sudoku = []
import random as r
for x in range(9):
   sudoku.append([r.randint(0,10) for x in range(9)])
for x in sudoku:
   print(x)
for x in range(9):
   for y in range(9):
      if sudoku[y][x] != sudoku[y][x] and if sudoku[x][y] != sudoku[x][y]:
         print("Valid!")
# not sure how to do 3x3 blocks

 
'''
    27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''
 
 
 
''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''