# 사용자로부터 두 개의 정수를 입력받아서 둘 중에서 큰 수를 출력하는 프로그램을 작성하여 보자.
first = int(input("첫 번째 정수: "))
second = int(input("두 번째 정수: "))
if first > second:
    print("큰 수는", first)
else:
    print("큰 수는", second)

