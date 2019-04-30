# 1부터 입력한 수 까지 더하기
# 1부터 사용자가 입력한 수 n까지 더해서 (1+2+3+...+n)을 계산하는 프로그램을 작성하여 보자.
# for문을 사용하면 간명하게 합계를 구할 수 있다.
number = int(input("자연수를 입력하세요: "))
sum = 0
for i in range(number + 1):
    sum += i
print("1부터 %d까지 더한 수는 %d입니다." %(number, sum))