# 팩토리얼을 계산하는 프로그램을 작성하여 보자.
# 팩토리얼 n!은 1부터 n까지의 정수를 모두 곱한 것을 의미한다.
# 즉, n! = 1 x 2 x 3 x ... x (n - 1) x n 이다.
# 예를 들어서 10!을 계산하는 프로그램을 작성하여 보자.
i = 1
factorial = 1
while (i <= 10):
    factorial *= i
    i += 1
print("10!은 %.2f입니다." %factorial)