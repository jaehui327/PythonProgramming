# 가위 바위 보
# 사용자가 가위, 바위, 보 중에서 하나를 선택하고 컴퓨터도 난수로 가위, 바위, 보 중에서 하나를 선택한다.
# 사용자의 선택과 컴퓨터의 선택을 비교하여서 승패를 화면에 출력한다.
from random import randint
user = input("(가위, 바위, 보) 중에서 하나를 선택하세요: ")
number = randint(0, 2)
li = ["가위", "바위", "보"]
computer = li[number]

if( user == computer):
    print("비겼습니다.")
elif(user == "가위" and computer == "바위"):
    print("컴퓨터가 이겼습니다.")
elif(user == "가위" and computer == "보"):
    print("사용자가 이겼습니다.")
elif(user == "바위" and computer == "보"):
    print("컴퓨터가 이겼습니다.")
elif(user == "바위" and computer == "가위"):
    print("사용자가 이겼습니다.")
elif(user == "보" and computer == "가위"):
    print("컴퓨터가 이겼습니다.")
elif(user == "보" and computer == "바위"):
    print("사용자가 이겼습니다.")
