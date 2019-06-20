# IMPORTING THE MODULE TURTLE
import turtle

# SETTING UP THE SCREEN
screen = turtle.Screen()
screen.bgcolor('black')
# SETTING UP TURTLE 1.0
sally = turtle.Turtle()
sally.color('white')

sally.speed(10)

# LOOP THAT REPEATS 180 TIMES
for i in range(180):
    sally.forward(100)
    sally.right(30)
    sally.forward(20)
    sally.left(60)
    sally.forward(50)
    sally.right(30)
    
    sally.penup()
    sally.setposition(0, 0)
    sally.pendown()
    
    sally.right(2)
    
# AFTER THE LOOP REPEATS 180 TIMES, THE TURTLE STOPS AND HIDES
turtle.done()
sally.hideturtle()
# DOING THE BORDER
pin = turtle.Turtle()
pin.color('white')

pin.penup()
pin.goto(-170, 170)

pin.speed(10)
pin.pendown()

for i in range(9):
    for i in range(40):
        pin.forward(20)
        pin.left(170)
        
    pin.penup()
    pin.left(38)
    pin.forward(40)
    pin.pendown()

turtle.done()
pin.hideturtle()
# THIS WAS FOR THE SECOND SET OF BORDERS
sue = turtle.Turtle()
sue.color('white')
sue.penup()
sue.goto(170, 170)
sue.forward(5)
sue.right(90)
sue.forward(40)

sue.speed(10)
sue.pendown()

for i in range(7):
    for i in range(40):
        sue.forward(20)
        sue.left(170)
    
    sue.penup()
    sue.left(38)
    sue.forward(40)
    sue.pendown()

sue.penup()
sue.right(60)
sue.forward(5)
sue.pendown()

for i in range(40):
    sue.forward(20)
    sue.left(170)

turtle.done()
sue.hideturtle()
#THIS IS FOR THIRD SET OF BORDERS
bee = turtle.Turtle()
bee.color('white')
bee.penup()
bee.goto(170, -170)
bee.forward(5)
bee.right(180)
bee.forward(40)

bee.speed(10)
bee.pendown()

for i in range(8):
    for i in range(40):
        bee.forward(20)
        bee.left(170)
      
    bee.penup()
    bee.left(38)
    bee.forward(40)
    bee.pendown()
    
turtle.done()
bee.hideturtle()
#  IT'S THE LAST PART OF THE BORDER
bob = turtle.Turtle()
bob.color('white')
bob.penup()
bob.goto( -170, -170)
bob.forward(5)
bob.left(90)
bob.forward(40)

bob.speed(10)
bob.pendown()

for i in range(7):
    for i in range(40):
        bob.forward(20)
        bob.left(170)
        
    bob.penup()
    bob.left(38)
    bob.forward(40)
    bob.pendown()
    
turtle.done()
bob.hideturtle()
