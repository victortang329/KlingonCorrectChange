"""
	MonChefDoeuvre1174.py

	Indoor scene using python turtle
	Child's toy rocket and flag, with starry ceiling

	Victor Tang	
	July 2017

"""


import turtle as t 
t.setup(800,600)
t.speed(3)
window = t.Screen()
window.bgcolor("peach puff")

# ideas for functions

def rectangle(side1, side2, lineColour, filledColour="none"):
	t.pencolor(lineColour)
	if filledColour != "none":
		t.fillcolor(filledColour)
		t.begin_fill()
	for i in range(2):
		t.forward(side1)
		t.left(90)
		t.forward(side2)
		t.left(90)
	if filledColour != "none":
		t.end_fill()
	return


def square(side, lineColour, filledColour="none"):
	t.pencolor(lineColour)
	t.pensize()
	if filledColour != "none":
		t.fillcolor(filledColour)
		t.begin_fill()
	for i in range(4):
		t.forward(side)
		t.left(90)
	if filledColour != "none":
		t.end_fill()
	return


def moveTo(positionX, positionY) :
	t.setheading(0)
	t.penup()
	t.goto(positionX, positionY)
	t.pendown()
	return


def triangle(side, lineColour, filledColour="none") :
	t.pencolor(lineColour)
	if filledColour != "none" :
		t.fillcolor(filledColour)
		t.begin_fill()
	for i in range(3):
		t.forward(side)
		t.left(120)
	if filledColour != "none" :
		t.end_fill()
	return

def star(side, lineColour, filledColour="none"):
	t.pencolor(lineColour)
	if filledColour != "none" :
		t.fillcolor(filledColour)
		t.begin_fill()
	for i in range(5):
		t.forward(side)
		t.right(144)
		t.forward(side)
	if filledColour != "none" :
		t.end_fill()
	return


def polygon(side, numSides, lineColour, filledColour="none"):
	t.pencolor(lineColour)
	t.pensize()
	angle = 360.0 / numSides
	if filledColour != "none":
		t.fillcolor(filledColour)
		t.begin_fill()
	for i in range(numSides):
		t.forward(side)
		t.left(angle)
	if filledColour != "none":
		t.end_fill()
	return


def doorknob(side, lineColour) :
	t.pencolor(lineColour)
	for i in range(50):
		t.forward(side)
		t.left(123)
	return

def circle(radius, lineColour, filledColour="none"):
	t.pencolor(lineColour)
	if filledColour != "none":
		t.fillcolor(filledColour)
		t.begin_fill()
	for i in range(radius):
		t.circle(radius)
	if filledColour != "none":
		t.end_fill()
	return


# floor
moveTo(-395, -290)
rectangle(780, 75, "black", "tan")

#ceiling
moveTo(-395, 99)
rectangle(780, 200, "black", "midnight blue")

# door
moveTo(-350, -215)
rectangle(120, 240, "black", "chocolate")
moveTo(-345, -210)
rectangle(50, 80, "black", "sienna")
moveTo(-285, -210)
rectangle(50, 80, "black", "sienna")
moveTo(-345, -75)
rectangle(50, 80, "black", "sienna")
moveTo(-285, -75)
rectangle(50, 80, "black", "sienna")
moveTo(-335, -100)
doorknob(10, "silver")

# door decoration
moveTo(-297, -50)
polygon(15, 8, "black", "red")


# rocket
moveTo(50, -215)
triangle(10, "black", "coral")
moveTo(70, -215)
triangle(10, "black", "coral")
moveTo(55, -205)
square(20, "black", "gold")
moveTo(55, -185)
triangle(20, "black", "teal")
moveTo(62, -205)
rectangle(6, 10, "black", "red")



# flag
moveTo(150, -215)
rectangle(5, 150, "black", "brown")
moveTo(155, -105)
t.left(30)
triangle(40, "black", "midnight blue")
moveTo(150, -65)
triangle(5, "black", "gold")

# stars
moveTo(-350, 230)
star(5, "yellow", "yellow")
moveTo(-326, 210)
star(5, "yellow", "yellow")
moveTo(50, 130)
star(5, "yellow", "yellow")
moveTo(100, 165)
star(5, "yellow", "yellow")
moveTo(-35, 260)
star(5, "yellow", "yellow")
moveTo(-70, 160)
star(5, "yellow", "yellow")
moveTo(350, 153)
star(5, "yellow", "yellow")
moveTo(290, 145)
star(5, "yellow", "yellow")
moveTo(105, 195)
star(5, "yellow", "yellow")
moveTo(283, 187)
star(5, "yellow", "yellow")
moveTo(300, 122)
star(5, "yellow", "yellow")
moveTo(329, 197)
star(5, "yellow", "yellow")


#clock
moveTo(15, -25)
polygon(25, 5, "grey", "orange")


