# sine graph 그리기
# 싸인(sine) 그래프를 반복문을 이용해서 그려보자.
# 싸인 함수는 수학, 물리학, 공학에서 아주 많이 나타나는 함수이다.
# 이번에도 터틀 그래픽의 기능을 사용하여 본다.
import math
import turtle
t = turtle.Turtle()
i = 0
for i in range(0, 360):
    angle = math.radians(i)
    t.goto(i, math.sin(angle) * 100)
