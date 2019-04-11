# 파이를 전역 변수로 이것을 이용하여서 원의 면적과 원의 둘레를 계산하는 작성해보자.
pi = 3.141592

def getArea(r):
    return pi * r**2

def getRround(r):
    return 2 * r * pi

r = int(input("원의 반지름을 읿력하세요: "))
print("원의 면적:", getArea(r))
print("원의 둘레:", getRround(r))