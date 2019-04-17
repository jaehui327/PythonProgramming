# 정수를 문자열로
# 파이썬의 내장 함수 str()을 사용하지 않고, 정수를 문자열로 바꾸어주는 함수를 정의하고 아래와 같이 출력해보자.
def intToString(i):
    s = ""
    while(1):
        if i == 0:
            return s
        s = str(i % 10) + s
        i = i // 10

i = int(input("정수 입력: "))
str = intToString(i)

print("입력된 숫자: %d" %i)
print("입력된 숫자의 형:", type(i))
print("변환된 숫자: %s" %str)
print("변환된 숫자의 형:", type(str))