# 이차방정식의 근 구하기
import math
print("이차방정식 ax^2 + bx + c 의 해를 구하겠습니다.")
a = int(input("a를 입력하세요: "))
b = int(input("b를 입력하세요: "))
c = int(input("c를 입력하세요: "))

D = b**2 - 4 * a * c
if a == 0 and b == 0:
    print("방정식이 아닙니다.")
elif a == 0:
    x = - c / b
    print("일차방정식 %dx + %d 는 해 %f 를 가집니다." % (b, c, x))
elif D == 0:
    x = -b / 2.0 * a
    print("이차방정식 %dx^2 + %dx + %d 는 중근 %f를 가집니다." %(a, b, c, x))
elif D > 0:
    x1 = (-b + math.sqrt(D)) / 2.0 * a
    x2 = (-b - math.sqrt(D)) / 2.0 * a
    print("이차방정식 %dx^2 + %dx + %d 는 서로 다른 두 근 %f, %f 를 가집니다." %(a, b, c, x1, x2))
else:
    print("이차방정식 %dx^2 + %dx + %d 는 해가 없습니다." %(a, b, c))
