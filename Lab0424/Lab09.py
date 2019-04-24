# 피타고라스 삼각형
# 피타고라스의 정리를 만족하는 삼각형들을 모두 찾아보자.
# 삼각형 한 변의 길이는 1부터 30 이하이다.
pytagoras = []
for a in range(1, 31):
    for b in range(a, 31):
        for c in range(b, 31):
            if (a ** 2 + b ** 2 == c ** 2):
                pytagoras.append((a, b, c))
print(pytagoras)

pytagoras2 = []
pytagoras2 = [(x, y, z) for x in range(1, 31) for y in range(x, 31) for z in range(y, 31) if x ** 2 + y ** 2 == z ** 2]
print(pytagoras2)