a = int(input("a를 입력하세요: "))
b = int(input("b를 입력하세요: "))
c = int(input("c를 입력하세요: "))

print("정렬 전: ", a, b, c)

if a > b:
    b,a = a,b
if b > c:
    c,b = b,c
if a > c:
    b,a = a,b

print("정렬 후: ", a, b, c)