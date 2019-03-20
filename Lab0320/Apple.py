fresh = input("사과가 신선하면 yes, 아니면 no를 입력하세요: ")
if fresh == "yes":
    cost = int(input("사과가 개당 얼마인가요? "))
    if cost > 1000:
        print("사과 5개를 구매합니다.")
    else:
        print("사과 10개를 구매합니다.")
elif fresh == "no":
    print("사과를 사지 않습니다.")
