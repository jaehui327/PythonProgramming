sum = 0
n = int(input("숫자를 입력하세요: "))
while n > 0:
    sum += int(n % 10)
    n /= 10
print("자릿수의 합은 %d입니다." %sum)