cost = float(input("구입 금액을 입력하시오: "))
if cost >= 100000:
    discount = cost * 0.05
    result = cost * 0.95
    print("구입 금액의 5퍼센트인 %.2f원 만큼 할인되어, 지불 금액은 %.2f원 입니다." %(discount, result))
else:
    print("지불 금액은 %")