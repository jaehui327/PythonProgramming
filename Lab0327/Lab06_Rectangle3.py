# 화면에 사각형 3개 그리기, 각 사각형은 20도씩 기울어져 있다
import turtle
t = turtle.Pen()
t.left(180)
for i in range(0, 3):
    t.right(20)
    for j in range(0, 4):
        t.forward(100)
        t.right(90)
