# 정수의 거듭제곱값을 계산하여 반환하는 함수를 작성하여 보자.
# (파이썬에는 ** 연산자가 있지만)
def power(x, y):
    result = 1;
    for i in range(0, y):
        result *= x;
    return result

print(power(3, 0))

# 재귀함수
def power2(x, y):
    if y != 0:
        return x * power(x, y - 1)
    else:
        return 1

print(power2(5, 0))
