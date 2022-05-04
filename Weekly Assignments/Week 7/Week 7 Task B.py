import turtle
from random import choice

t=turtle.Turtle()

directions = [0, 90, 180, 270]

running = True
def randomWalk():
    while running:
        t.setheading(choice(directions))
        t.forward(50)
        
randomWalk()