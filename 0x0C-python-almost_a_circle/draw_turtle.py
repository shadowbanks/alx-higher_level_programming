#!/usr/bin/python3
import turtle


will = turtle.Turtle()

will.color("green", "cyan")

will.begin_fill()
will.forward(100)
for i in range(3):
    will.left(90)
    will.forward(100)
will.end_fill()

turtle.done()
