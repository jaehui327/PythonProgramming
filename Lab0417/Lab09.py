# 문자열을 조사하여서 알파벳 문자의 개수, 숫자의 개수, 스페이스의 개수를 출력하는 프로그램을 작성하라.
alphabetNum = 0
spaceNum = 0
numberNum = 0
s = input("문자열을 입력하세요: ")

for c in s:
    if c.isalpha():
        alphabetNum += 1
    elif c.isspace():
        spaceNum += 1
    elif c.isnumeric():
        numberNum += 1
print("알파벳 문자의 개수: %d" %alphabetNum)
print("숫자 문자의 개수: %d" %numberNum)
print("스페이스 문자의 개수: %d" %spaceNum)