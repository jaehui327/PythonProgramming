# 육각형 그리기
# 터틀 그래픽을 이용하여 다각형을 화면에 그려보자.
import turtle
figure = turtle.Pen()
for i in range(0, 6):
    figure.forward(100)
    figure.right(60)