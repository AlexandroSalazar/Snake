from ast import While
from random import random
from re import X
from tracemalloc import stop
import turtle
import time


delay = 0.1

wn = turtle.Screen()

#Tittle
wn.title("Snake Game")

#windows Size
wn.setup(width=600, height=600)

#background color
wn.bgcolor("light blue")

#Head Settings

#Turtle Obj
Head = turtle.Turtle()

#seet the pointer
Head.speed(0)

#shape head
Head.shape("square")

#head color
Head.color("green")

#no drawing moving snake
Head.penup()

#center head
Head.goto(0, 0)

#wait the direction order
Head.direction = "stop"

#food setting
Food = turtle.Turtle
Food.speed(0)
Food.shape("circle")
Food.color("Red")
Food.penup()
Food.goto(0, 100)
Food.direction = "stop"



def mov():
    
    if Head.direction == "up":
    
        #current coordinate Y
        Y = Head.ycor()
        Head.sety(Y + 10)
        
    if Head.direction == "down":
        
        #current coordinate Y
        Y = Head.ycor()
        Head.sety(Y - 10)
        
    if Head.direction == "left":
        
        #current coordinate X
        X = Head.xcor()
        Head.setx(X - 10)
        
    if Head.direction == "rigth":
        
        #current coordinate X
        X = Head.xcor()
        Head.setx(X + 10)


def dirUp():
    Head.direction = "up"
    
def dirDown():
    Head.direction = "down"
    
def dirRigth():
    Head.direction = "rigth"
    
def dirLeft():
    Head.direction = "left"



#conect to keyboard
wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirRigth, "Right")
wn.onkeypress(dirLeft, "Left")

while True:
    wn.update()
    
    if Head.distance(Food) < 20:
        X = random.daint(-280, 280)
        Y = random.daint(-280, 280)
        
    mov()
    time.sleep(delay)


turtle.done()