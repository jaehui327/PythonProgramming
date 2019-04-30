# 사용자로부터 정수를 음수, 0, 양수 중의 하나로 분류하여 보자.
integer = int(input("정수를 입력하세요: "))
if integer > 0:
    print("입력된 정수는 양수입니다.")
elif integer < 0:
    print("입력된 정수는 음수입니다.")
else:
    print("입력된 정수는 %d입니다" %integer)
