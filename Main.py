# import colorgram
#
# rgb_color = []
# colours = colorgram.extract("palatte.jpg", 50)
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

import turtle as t
import random

tim = t.Turtle()
t.title('Million Dollar Painting')
#t.bgcolor("#DBE9EE")
t.colormode(255)
tim.speed("fastest")
colors = [(235, 234, 233), (233, 234, 237), (235, 238, 236), (235, 226, 230), (208, 164, 111), (18, 25, 53), (226, 207, 131), (141, 62, 93), (204, 132, 147), (208, 80, 105), (84, 116, 97), (64, 93, 137), (131, 153, 142), (68, 20, 38), (126, 33, 56), (143, 157, 175), (40, 53, 104), (141, 73, 57), (225, 181, 165), (228, 165, 180), (94, 126, 170), (112, 135, 123), (184, 188, 204), (168, 114, 97), (38, 82, 62), (183, 200, 178), (201, 118, 47), (25, 68, 48), (98, 50, 23), (45, 69, 78), (180, 197, 199), (98, 56, 31)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(20):
    for _ in range(20):
        tim.dot(15, random.choice(colors))
        tim.forward(25)
    tim.left(90)
    tim.forward(25)
    tim.left(90)
    tim.forward(500)
    tim.right(90)
    tim.right(90)

screen = t.Screen()
screen.exitonclick()