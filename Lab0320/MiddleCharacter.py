s = input("문자열을 입력하시오: ")
n = len(s)
if (n % 2) == 0:
    print("중앙 글자는", s[n//2 - 1] + s[n//2])
else:
    print("중앙 글자는", s[n//2])
