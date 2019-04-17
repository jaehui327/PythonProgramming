# 문자열을 조사하여서 알파벳 문자의 개수, 숫자의 개수, 스페이스의 개수를 출력하는 프로그램을 작성하라.
alphabetNum = 0
spaceNum = 0
numberNum = 0
s = input("문자열을 입력하세요: ")

for c in s:
    if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
        alphabetNum += 1
    elif ord(c) == 32:
        spaceNum += 1
    elif ord(c) >= 48 and ord(c) <= 57:
        numberNum += 1
print("알파벳 문자의 개수: %d" %alphabetNum)
print("숫자 문자의 개수: %d" %numberNum)
print("스페이스 문자의 개수: %d" %spaceNum)