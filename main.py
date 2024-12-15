
# import colorgram
# colors = colorgram.extract('hirst.jpg',100)
# l = []
# for _ in colors:
#     r = _.rgb[0]
#     g = _.rgb[1]
#     b = _.rgb[2]
#     t = (r, g, b)
#     l.append(t)
# print(l)

import random
import turtle as t
from turtle import Turtle, Screen


tim = Turtle()
# tim.shape("circle")
# tim.pensize(20)
tim.shape("circle")
# tim.pencolor("green")
screen = Screen()
screen.colormode(255)

def r_color():
    l = [(215, 166, 17), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166),
             (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173),
             (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198),
             (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56), (11, 87, 108), (177, 190, 213),
             (111, 124, 153), (81, 142, 169), (73, 63, 53)]

    color = random.choice(l)
    return color
tim.dot(20,r_color())


t.speed("fastest")

rs = False
for _ in range(10):
    for _ in range(10):
        tim.dot(20,r_color())
        tim.forward(1)
        tim.penup()
        tim.forward(40)
        tim.pendown()
        tim.dot(20,r_color())
        tim.forward(1)
    if rs==True:
        tim.left(90)
        tim.penup()
        tim.forward(40)
        tim.pendown()
        tim.dot(20,r_color())
        tim.forward(1)
        tim.left(90)
        rs = False
    else:
        tim.right(90)
        tim.penup()
        tim.forward(40)
        tim.pendown()
        tim.dot(20,r_color())
        tim.forward(1)
        tim.right(90)
        rs = True


screen.exitonclick()