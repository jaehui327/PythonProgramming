# 생일 축하 메시지를 출력하는 함수 happyBirthday()를 작성해보자.
def happyBirthday():
    i = 0
    while(1):
        if i >= 3:
            break
        if i == 2:
            print("사랑하는 친구의", end = " ")
        print("생일축하 합니다!")
        i += 1

happyBirthday()