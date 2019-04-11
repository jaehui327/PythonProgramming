# 섭씨 온도를 회씨 온도로 변환하여 반환하는 함수 FtoC()를 작성하고 테스트하라.
# (C = (F - 32) * 5 / 9)
def FtoC(t):
    return (t - 32) * 5 / 9

temp = float(input("화씨온도를 입력하시오: "))
print(FtoC(temp))