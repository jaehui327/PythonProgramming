# 여기서는 소수를 판별하는 함수 is_prime()을 작성하여 사용하여 보자.
def is_prime(i):
    for x in range(2, i):
        if i % x == 0:
            return False
    return True

integer = int(input("정수를 입력하시오: "))
print(is_prime(integer))