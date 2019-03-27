# sine graph 그리기
import math
import turtle
t = turtle.Turtle()
i = 0
for i in range(0, 360):
    angle = math.radians(i)
    t.goto(i, math.sin(angle) * 100)
