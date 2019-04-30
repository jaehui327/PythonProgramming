# for문을 이용해서 팩토리얼을 계산해보자.
# 팩토리얼 n!은 1부터 n까지의 정수를 모두 곱한 것을 의미한다.
# 즉, n! = 1 x 2 x 3 x ... x (n-1) x n 이다.
limit = int(input("정수를 입력하세요: "))
multiple = 1
for i in range(1, limit + 1):
    multiple *= i
print("%d!는 %.1f입니다." %(limit, multiple))