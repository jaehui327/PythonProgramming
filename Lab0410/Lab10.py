# 2차원 평면에서 2개의 점을 입력 받았을 때, 2점을 지나는 직선의 기울기와 y 절편을 반환하는 함수를 작성하시오.
def get_line(x1, x2, y1, y2):
    if x1 == x2:
        return 0, 0
    else:
        slope = (float)(y2 - y1) / (float)(x2 - x1)
        yIntercept = y1 - slope * x1
        return slope, yIntercept # 2개의 값을 반환한다.

x1 = int(input("x1= "))
x2 = int(input("x2= "))
y1 = int(input("y1= "))
y2 = int(input("y2= "))
slope, yIntercept = get_line(x1, x2, y1, y2) # 반환된 값을 풀어서 변수에 저장한다.
print("기울기=", slope, "y절편=", yIntercept)