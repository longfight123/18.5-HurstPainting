"""

This script creates a 'Hurst painting' using the
'turtle' module on the screen.

This script requires that 'turtle' and 'colorgram' be installed within the Python
environment you are running this script in. 

"""

import turtle
import colorgram
import random

colors = colorgram.extract('.\\hirst_painting.jpg', 30)
colors_list = []
for _ in colors:
    # each color object has an attribute rgb which
    # returns a named tuple of rgb colors.
    # To access r, g or b values use r, g or b for the named tuple
    colors_list.append((_.rgb.r, _.rgb.g, _.rgb.b))
# This line of code is to get rid of the white colors
# the closer the values are 255, the more likely it is white
colors_list = colors_list[4:]

tim = turtle.Turtle()
turtle.colormode(255)
for column in range(10):
    for row in range(10):
        tim.pencolor(random.choice(colors_list))
        tim.dot(size=20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.backward(50*10)
    tim.left(angle=90)
    tim.forward(50)
    tim.right(angle=90)
    tim.pendown()

screen = turtle.Screen()
screen.exitonclick()
