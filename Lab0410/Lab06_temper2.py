# 섭씨 온도를 화씨 온도로, 또 그 반대로 변환하는 프로글매을 작성하여 보자.
# C = (F - 32) * 5 / 9
# F = C * 9 / 5 + 32
def FtoC(t):
    return (t - 32) * 5 / 9
def CtoF(t):
    return t * 9 / 5 + 32

while(1):
    print("'c' 섭씨온도에서 화씨온도로 변환")
    print("'f' 화씨온도에서 섭씨온도로 변환")
    print("'q' 종료")
    op = input("메뉴에서 선택하세요: ")
    if op == 'c':
        c = float(input("섭씨 온도: "))
        print("화씨 온도: ", CtoF(c))
    elif op == 'f':
        f = float(input("화씨 온도: "))
        print("섭씨 온도: ", FtoC(f))
    elif op == 'q':
        break
    else:
        print("잘못된 문자가 입력되었습니다.")

