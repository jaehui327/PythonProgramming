# 변수 값 교환
x = 10
y = 20
print("x: ", x, " y: ", y)
print("변수 값을 교환합니다.")
temp = x
x = y
y = temp
print("x: ", x, " y: ", y)
print("변수 값을 교환합니다.")
(x, y) = (y, x)
print("x: ", x, " y: ", y)
