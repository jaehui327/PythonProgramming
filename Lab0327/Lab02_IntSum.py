# 1부터 입력한 수 까지 더하기
number = int(input("자연수를 입력하세요: "))
sum = 0
for i in range(number + 1):
    sum += i
print("1부터 %d까지 더한 수는 %d입니다." %(number, sum))