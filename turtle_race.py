import turtle as t
from random import *
screen = t.Screen()
p1 = t.Turtle()
p2 = t.Turtle()
p1.color("green")
p2.color("blue")
p1.shape("turtle")
p2.shape("turtle")
p1.penup()
p2.penup()
p1.goto(300,60)
p2.goto(300, -140)
p1.pendown()
p2.pendown()
p1.circle(40)
p2.circle(40)
p1.penup()
p2.penup()
p1.goto(-200, 100)
p2.goto(-200, -100)
p1.pendown()
p2.pendown()
for i in range(20):
    p1pos = p1.pos()
    p2pos = p2.pos()   
    if 250 <= p1.xcor() <= 350:
        print("p1 has won the game! ")
        break
    elif 250 <= p2.xcor() <= 350:
        print("p2 has won the game! ")
        break
    dice = randint(1, 6)
    p1.forward(20 * dice)    
    dice = randint(1, 6)
    p2.forward(20 * dice)    
t.mainloop