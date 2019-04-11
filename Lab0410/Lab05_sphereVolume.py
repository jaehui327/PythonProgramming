# 구의 부피를 계산하는 함수 sphereVolume()을 작성하여 보자.
# 반지름이 r인 구의 부피는 다음과 같다.
# V = 4 / 3 * 3.141592 * r^3
import math
def sphereVolume(r):
    return 4 / 3 * math.pi * r**3
r = float(input("구의 반지름을 입력하세요: "))
print(sphereVolume(r))