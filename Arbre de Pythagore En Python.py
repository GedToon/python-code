import turtle
from turtle import *
speed(0)
angle = 30
color("darkred")

def arbre(n, longueur):
    if n == 0:
        color("green")
        forward(longueur)
        back(longueur)
        color("darkred")
    else:
        width(n)
        forward(longueur/3)
        left(angle)
        arbre(n-1,longueur/3*2)
        right(2 * angle)
        arbre(n-1, longueur/3*2)
        left(angle)
        back(longueur/3)

hideturtle()
up()
right(90)
forward(300)
left(180)
down()
arbre(10,700)
showturtle()
# keep window open
mainloop()
