# 두 개의 정수가 주어지면 두 수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수를 만들어보자.
def get_max(a, b):
    if a > b:
        return a
    else:
        return b
print(get_max(10, 20))
