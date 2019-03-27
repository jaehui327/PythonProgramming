limit = int(input("정수를 입력하세요: "))
multiple = 1
for i in range(1, limit + 1):
    multiple *= i
print("%d!는 %.1f입니다." %(limit, multiple))