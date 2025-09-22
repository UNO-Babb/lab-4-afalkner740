#TurtleGraphics.py
#Name: Alexa Falkner
#Date: 9/21
#Assignment: Turtle

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.left(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)

def fillCorner(alice, corner):
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        
    elif corner == 2:
        alice.forward(50)
        alice.forward(50)
        alice.left(90)
        alice.begin_fill()
        alice.forward(50)
        drawSquare(alice,50)
        alice.end_fill()


def main():
    myTurtle = turtle.Turtle()
    wn = turtle.Screen()
    wom = turtle.Turtle()
    sizevar = 100
    for i in range(5):
       draw_square(wom, sizevar)
       sizevar += 40
       wom.penup()
       wom.backward(20)
       wom.right(90)
       wom.forward(20)
       wom.left(90)
       wom.pendown()
fillCorner(myTurtle,2)

main()
