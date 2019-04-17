# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자.
# 사용자는 1000워짜리 지폐와 500원짜리 동전, 100원짜리 동전을 사용할 수 있다.
# 물건값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 거스름돈을 계산하여서 동전으로 반환한다.
price = int(input("물건값을 입력하세요: "))
thousandNum = int(input("1000원 지폐 개수: "))
fiveHundredNum = int(input("500원 동전개수: "))
oneHundredNum = int(input("100원 동전개수: "))
remain = 1000 * thousandNum + 500 * fiveHundredNum + 100 * oneHundredNum - price

remain500Num = remain // 500
remain100Num = (remain - 500 * remain500Num) // 100
remain10Num = (remain - 500 * remain500Num - 100 * remain100Num) // 10
remain1Num = remain - 500 * remain500Num - 100 * remain100Num - 10 * remain10Num

print("500원= %d, 100원= %d, 10원= %d, 1원= %d" %(remain500Num, remain100Num, remain10Num, remain1Num))