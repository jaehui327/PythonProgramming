import turtle
t = turtle.Pen()
while True:
    direction = input("왼쪽은 left, 오른쪽은 right, 멈추려면 stop을 입력하세요: ")
    if direction == "left":
        t.left(60)
        t.forward(50)
    elif direction == "right":
        t.right(60)
        t.forward(50)
    elif direction == "stop":
        break
