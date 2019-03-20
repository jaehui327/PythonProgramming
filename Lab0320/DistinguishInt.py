integer = int(input("정수를 입력하세요: "))
if integer > 0:
    print("입력된 정수는 양수입니다.")
elif integer < 0:
    print("입력된 정수는 음수입니다.")
else:
    print("입력된 정수는 %d입니다" %integer)
