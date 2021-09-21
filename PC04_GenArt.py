"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Tala Vicknair

********* HEY, READ THIS FIRST **********

This piece is the same as my previous project for PC03, but the colors are random as well as adding a border
I like pink and green and the combination is one of my favorites, I thought it would be fun to see where it could go and how it could change.
The grey border makes the lines stand out more, and I think it looks really cool.
The lines can be random in color and height, the triangles are different shades of grey.

"""
import turtle
import random

turtle.colormode(255)


# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
panel.bgcolor(85,85,85)

xCoords = (-300,-200,-100,0,100,200,300)
lineTop = (150,125,100,75,50)
lineBot = (-150,-125,-100,-75,-50)
lineRepeats = 3
triRepeats = range(0,16)
TriTop = 200
TriBot = -200
tColors = ("gray50","gray60","gray70","gray80") #Multiple color options for more possible variation
pColors = ("HotPink3","maroon3","MediumOrchid1","pink","VioletRed")
gColors = ("PaleGreen2","MediumSeaGreen","DarkOliveGreen1","GreenYellow","LimeGreen")

pink = turtle.Turtle()
pink.pensize(3)
pink.color(random.choice(pColors)) #this will pick a random pink color from the tuple above
pink.speed(10)
green = turtle.Turtle()
green.pensize(3)
green.color(random.choice(gColors)) #this will pick a random green color from the tuple above
green.speed(10)
tri = turtle.Turtle()
tri.hideturtle()
tri.shape("triangle")
tri.speed(0)
tri.turtlesize(2,2)

pink.up()
green.up()
tri.up()

tri.goto(xCoords[0], TriTop)

#each random.choice(line___) below will select a different y coordinate from the list above
#this will change the height of the point each time the code runs
#I couldn't figure out how to include increments in for loops, which is what I attempted first
pink.goto(xCoords[0], random.choice(lineBot))
green.goto(xCoords[0], random.choice(lineTop))
pink.down()
green.down()
pink.goto(xCoords[1], random.choice(lineTop))
green.goto(xCoords[1], random.choice(lineBot))
pink.goto(xCoords[2], random.choice(lineBot))
green.goto(xCoords[2], random.choice(lineTop))
pink.goto(xCoords[3], random.choice(lineTop))
green.goto(xCoords[3], random.choice(lineBot))
pink.goto(xCoords[4], random.choice(lineBot))
green.goto(xCoords[4], random.choice(lineTop))
pink.goto(xCoords[5], random.choice(lineTop))
green.goto(xCoords[5], random.choice(lineBot))
pink.goto(xCoords[6], random.choice(lineBot))
green.goto(xCoords[6], random.choice(lineTop))

#This will repeat 2 triangles being stamped enough times to cover the screen without going for too long, which I found to be 31 times
#This for loop is for the top stripe of triangles
tri.showturtle()
for i in triRepeats:
    tri.color(random.choice(tColors)) #this will pick a random gray shade from the options above
    tri.left(90)
    tri.stamp()
    tri.right(90)
    tri.forward(20)
    tri.right(90)
    tri.backward(10)
    tri.color(random.choice(tColors))
    tri.stamp()
    tri.forward(10)
    tri.left(90)
    tri.forward(20)
    
#tri.goto(xCoords[0], TriBot)

#This for loop is for the bottom stripe of triangles
for i in triRepeats:
    tri.color(random.choice(tColors))
    tri.left(90)
    tri.stamp()
    tri.right(90)
    tri.forward(20)
    tri.right(90)
    tri.backward(10)
    tri.color(random.choice(tColors))
    tri.stamp()
    tri.forward(10)
    tri.left(90)
    tri.forward(20)

turtle.done()