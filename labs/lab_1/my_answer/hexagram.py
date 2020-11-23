# Written by Vincent Yuchen Yan for comp9021 lab1

'''
draws an hexagram that is centred horizontally in the
window that
displays it, with the colour of the tips alternating red and blue
'''
from turtle import *


def draw_red(color_1):
    left(60)
    color(color_1)
    for _ in range(3):
        forward(50)
        right(120)
        forward(50)
        penup()
        forward(50)
        pendown()
        
def draw_blue(color_2):
    left(60)
    color(color_2)
    for _ in range(3):
        forward(50)
        right(120)
        forward(50)
        penup()
        forward(50)
        pendown()   

draw_red('red')
penup()
backward(50)
pendown()
draw_blue('blue')
