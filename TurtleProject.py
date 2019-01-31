# Before you can use any off these functions, you first have to import turtle
# Make little independent scenarios
import turtle

# 1) Draw

# Moves the "turtle" forward by a specified distance in the direction it's facing. You can use either method.
# In this example, the turtle moves forward 100 steps
distance = 100
turtle.forward(distance)
turtle.fd(distance)

# Moves the "turtle" backward by a distance in the opposite direction that it's facing. You ca use any of the following methods.
# In this example, the turtle moves backward 100 steps
turtle.backward(distance)
turtle.back(distance)
turtle.bk(distance)

# Turns the turtle left by a specified angle; units are in degrees by default. You can use either method.
# This example has the turtle turning 90 degrees to the left
angle = 90
turtle.left(angle)
turtle.lt(angle)

# Turns the turtle right by an angle; units are in degrees by default. You can use either method.
# This example had the turtle turing 90 degrees to the right
turtle.right(angle)
turtle.rt(angle)

# Moves the turtle to a different position; if the "pen" is down, it draws a line.
# Accepts x and y coords., but you can use a pair of numbers for your x coord. and have it accept nthing for your y coord.
# You can use any of these methods
turtle.goto(20,20)
turtle.setpos((60,40))
turtle.setposition(0,0)

# Only sets the turtle's x coord.
x = 10
turtle.setx(x)

# Only sets the turtle's y coord.
y = 10
turtle.sety(y)

# Sets the orientiation of the turtle to an angle. You can use either method.
# In standard mode, 0 degrees is east, 90 degrees in north, 180 degrees is west, 270 is south
angle = 180
turtle.setheading(angle)
turtle.seth(0)

# Moves the turtle back to the origin (0,0) and sets its heading to its original orientation.
turtle.home()

# Draws a circle with a given radius, and an optionally given extent and steps
# The center of the circle is left of turtle
# The extent of the circle is how far you want to draw the circle; the accepted number is i degrees
# The number of steps it takes for the circle to be drawn is equivalent to how many sides the shape has (or how many "strokes" it takes to draw), so this can be used to draw regular polygons
# If the given radius is positive, it will draw the circle or arc counterclockwise; otherwise it will draw it clockwise
# The direction of the circle to change by the extent of the drawn circle
# In this example, a circle with a radius of 50 is being draw in 5 steps; this draws a regular pentagon
# The definition of a regular polygon is a polygon with 'n' sides where each angle and side is the same measurement
radius = 50
extent = 360
steps = 5
turtle.circle(radius, extent, steps)

# Draws a circular dat with a specified diameter using a specified color
# If the size is not given, the maximum of pensize+4 and 2*pensize is used (pensize default is 1)
# The diameter has to be greater than or equal to 1
# The color can be a string or a numeric color tuple
turtle.dot(10, "green")

# Stamps a copy of the turtle's shape onto the picutre/canvas as the turtle's current position
# It returns a stamp ID for that specific stamp, which can be used to delete it
turtle.stamp()

# Deletes a specified stamp using it's attributed stamp ID
stampID = 5
turtle.clearstamp(stampID)

# Deletes all turtle stamps
# If there is no parameter (a number), then it deletes all stamps
# If there is a positive parameter, it deletes the first 'n' stamps
# If there is a negative parameter, it deltes the last 'n' stamps
turtle.clearstamps()

# Undoes the the turtle's last action
turtle.undo()

# Set's the turtle's speed between 0 and 10
# If the speed is 0, then there is no drawing animation
# If the inputed speed is greater than 10 or less than .5, then speed is set to 0
# If there is no inputed speed, then it returns the current speed value
# You can also use speed strings: fastest = 0, fast = 10, normal = 6, slow = 3, slowest = 1
turtle.speed("fastest")
turtle.speed(1)
turtle.speed()

# ------------------------------------------

#The Turtle's Postions

# Returns the current location of the turtle as coordinates.
# Either method works
turtle.position()
turtle.pos()

# Returns the angle of line between the turtle's postion and the position specified by coordinates of another turtle
# You can either use an x and y value, or your x value can be a pair of coordinates
turtle.towards(0,0)

# Returns the turtle's x coord.
turtle.xcor()

# Returns the turtle's y coord.
turtle.ycor()

# Returns the turtle's current orientation or heading
turtle.heading()

# Returns the distance from the turtle to a given coordinate or other turtle
# You can either give an x and y value, or your x value can be a pair of coordinates
turtle.distance(50,50)

# --------------------------------------

#Measurement

# Set angle measurement units (set numbr of "degree" for a full circle)
# Default value is 360 degrees
turtle.degrees(360)

# Set the angle measurement units to radians
# Radians are equivalent to degrees(2*math.pi)
turtle.radians()

# -----------------------------------------

#Drawing State

# Pulls the pen up (no drawing when the turtle moves)
turtle.penup()
turtle.pu()
turtle.up()

# Puts the pen down (draws when the turtle moves)
# You can use any of these methods
turtle.pendown()
turtle.pd()
turtle.down()

# Returns the pen's attributes in a dictionary
# Tells you pen color, whether the pen is down or up, pensize, speed, etc.
# The dictionary can be used as the pen argument, where pen is a dictionary
# The pendict parameter is one of more of the keyword arguments that are in the list
penstate = turtle.pen()
turtle.pen(penstate, fillcolor = "yellow")

# Returns True is the pen is down and False if it's up
turtle.isdown()

# -----------------------------------------------

#Color

# Returns or sets the pen color
# Can accept a colorstring (includes hex codes in the form of strings)
# Can accept and RGB value in the form of a tuple or individual numbers
turtle.colormode(255)
turtle.pencolor()
turtle.pencolor("red")
turtle.pencolor("#ff6100")
turtle.pencolor((0,255,0))
turtle.pencolor(0,0,255)

# Returns or sets the fill color
# Accepts the same arguments as pencolor
turtle.colormode(255)
turtle.fillcolor()
turtle.fillcolor("red")
turtle.fillcolor("#ff6100")
turtle.fillcolor((0,255,0))
turtle.fillcolor(0,0,255)

# Returns or sets the pen and fill color
# Accepts the same arguments and pencolor
turtle.color()
turtle.color("blue") #sets both pen and fill color
turtle.color((255,0,0),(0,255,0)) #sets pen color first, then fill color second

# ------------------------------------------

#Fill

# Returns the fill state (True if there is fillig, False if not)
turtle.filling()

# Is called before drawing a shape that is going to be filled
turtle.begin_fill()

# Fills the shape rawn after the last begin_fill call
turtle.circle(100)
turtle.end_fill()

# ---------------------------------------------

#Drawing Control

# Resets canvas and turtle
turtle.reset()

# Deletes the turtle's drawings, but does not affect the turtle
turtle.clear()

# Write text
# The four arguments in order are the string of text, whether you want to move the pen,
# how you want to align it, and the font
turtle.write("This is text!", True, align = "center", font = ("Calibri",12,"bold"))

# -----------------------------------------------

#Turtle Visibility

# Makes the turtle invisible. Both methods work
turtle.hideturtle()
turtle.ht()

# Makes the turtle visible
turtle.showturtle()
turtle.st()

# Tells you if your turtle is visible or not
# Returns true is visible
turtle.isvisible()

# ------------------------------------------------

#Turtle Appearance

# Sets the turtle shape to a given, valid shapename in the form of a string
# If there is no given shapename, then it returns the current turtle shape
turtle.shape("triangle")
turtle.shape()

# Chanes the size of the turtle; if no string is given, then it returns the current resize mode
# "auto": changes the turtle corresponding to the pensize
# "user": changes the turtle according to the stretch factor and outline width
# "noresize": no change is made to the turtle appearance
turtle.resizemode("auto")

# Returns or sets the pen's attributes (x/y stretchfactors and/or outline)
# First value is the stretch width, second is the stretch len, and third is the outline; all values are positive
# Either method works
turtle.shapesize(2, 3, 6)
turtle.turtlesize()


#Using Events (?)
#Special Turtle Fuctions/Methods
#Window Control
#Animation Control
#Using Screen Events (?)
#Settings (and special methods?)
#Input Functions (?)
#Screen-Specific Methods
