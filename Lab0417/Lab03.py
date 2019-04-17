# 상점 주인 A씨는 손님을 위해 거스름돈을 최소의 지폐와 동전으로 주려 한다.
# A씨는 이를 자동으로 계산해주는 프로그램을 필요로 한다.

# A씨를 위해 물건값과 손님이 지불한 돈이 입력되었을 때, 만원, 오천원, 천원, 오백원, 오십원, 십원, 일원 단위로 각각 얼마나 손님에게 주어야 하는지 출력해주는 프로그램을 작성해보자.
# 단, 손님이 물건 값 보다 적은 돈을 지불하였을 경우 프로그램을 종료되어야 한다.
# 힌트: 프로그램 종료는 exit(1)이란 코드로 수행할 수 있다.

productPrice = int(input("물건의 가격을 입력하세요: "))
money = int(input("지불할 금액을 입력하세요: "))
if productPrice > money:
    print("손님이 물건 값 보다 적은 돈을 지불했습니다.")
    exit(1)
remain = money - productPrice
print("거스름돈:", remain)

print("만원: %d장" %(remain // 10000))
remain = remain % 10000
print("천원: %d장" %(remain // 1000))
remain = remain % 1000
print("백원: %d개" %(remain // 100))
remain = remain % 100
print("십원: %d개" %(remain // 10))
remain = remain % 10
print("일원: %d개" %(remain))
