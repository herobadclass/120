
import turtle as t
import random as r

def move(num2):
    t.penup()
    t.backward(num2)
    t.left(90)
    t.forward(5)
    t.pendown()

def size1(num1,num2):
    t.pensize(1)
    for i in range(num1):
        t.right(90)
        t.forward(num2)
        move(num2)

def size2(num1,num2):    
    t.pensize(2)
    for i in range(num1):
        t.right(90)
        t.forward(num2)
        move(num2)

def size4(num1,num2):
    t.pensize(1)
    for k in range(num1):
        colour = (255,255,255)
        while colour == (255,255,255):    
            colour = (255*r.randint(0,1),255*r.randint(0,1),255*r.randint(0,1))
        t.fillcolor(colour)
        t.pencolor(colour)
        t.begin_fill()
        for i in range(2):
            t.forward(4)
            t.right(90)
            t.forward(num2)
            t.right(90)
        t.end_fill()
        t.penup()
        t.forward(10)
        t.pendown()
    t.fillcolor(0,0,0)
    t.pencolor(0,0,0)

#TOP
    
t.colormode(255)
size1(2,100)
size4(1,100)
size2(1,100)
size2(2,90)
size4(2,90)
size1(1,90)
size2(1,90)
size1(2,100)
size1(1,90)
size2(2,90)
size1(1,90)
size2(1,90)
size4(1,90)
size2(1,100)
size4(1,100)
size1(2,100)
t.penup()
t.forward(100)
