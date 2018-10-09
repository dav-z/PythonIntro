## David Zheng
## Lab 7 Turtle drawing template
##   be sure to add your name, date and change file name

import turtle
from random import choice
#from PickColor import *

def main():
    ## Create turtle,
    ## DO NOT create a turtle window first (no:  screen = turtle.Screen())
    franklin = turtle.Turtle()
    franklin.speed(1000)
    franklin.penup()
    spiral(franklin, 6, 10000)
    spiral2(franklin, 3, 100)
    print('My turtle is an artist!')
    # _____  = turtle.Turtle()

    ## Set up  turtle and call functions that draw       
    pass

##########################################################
## Create functions to make the picture


def spiral(n, s, y):
    colors = ['pink', 'orange', 'pink', 'orange', 'pink', 'orange']
    n.pendown()
    n.speed(y)
    for x in range(360):
        n.pencolor(colors[x%s])
        n.forward(x*3/s+x)
        n.left(360/s+1)
        n.width(x*s/100)

def spiral2(n, s, y):
    colors = ['lime green', '#663399', 'lime green', '#663399', 'lime green', '#663399']
    n.penup()
    n.goto(0,0)
    n.pendown()
    n.speed(y)
    for x in range(360):
        n.pencolor(colors[x%s])
        n.forward(x*3/s+x)
        n.right(360/s+1)
        n.width(x*s/200)


####  Using MAIN to call all code ########################  
if __name__ == '__main__':
    
    main()    

