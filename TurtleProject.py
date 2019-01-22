#Before you can use any off these functions, you first have to import turtle

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

#The Turtle's Postions
#Measurement
#Drawing State
#Color
#Fill(ing)
#Drawing Control
#Turtle Visibility
#Turtle Appearance
#Using Events (?)
#Special Turtle Fuctions/Methods
#Window Control
#Animation Control
#Using Screen Events (?)
#Settings (and special methods?)
#Input Functions (?)
#Screen-Specific Methods
