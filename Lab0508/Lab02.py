# 함수의 튜플 반환 예제
# 원의 넓이와 둘레를 동시에 반환하는 함수를 작성, 테스트해보자.
# 출력 결과
# 원의 반지름을 입력하시오: 10
# 원의 넓이는 314.159265358973이고 원의 둘레는 62.83185307179586이다.

import math

def calCircle(r):
    # 반지름이 r인 원의 넓이와 둘레를 동시에 반환하는 함수 (area, circum)
    area = math.pi * r * r
    circum = 2 * math.pi * r
    return (area, circum)

radius = float(input("원의 반지름을 입력하시오: "))
# area = math.pi * radius**2
# round = 2 * math.pi * radius
# print("원의 넓이는 %.13f이고 원의 둘레는 %.14f이다. " %(area, round))
(a, c) = calCircle(radius)
print("원의 넓이는 %s이고 원의 둘레는 %s이다. " %(str(a), str(c)))