i = 1
x = 3
sum = 0
while (i <= 100):
    if (i % 3 == 0):
        sum += i
    i += 1
print("1부터 100 사이의 모든 %d의 배수의 합은 %d입니다." %(x, sum))
