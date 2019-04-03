# 문자열 중에서 자음과 모음의 개수를 집계하는 프로글매을 작성하여 보자.
# 문자열 소문자 변환: stringVar.lower()
# 문자열 알파벳만 포함 여부: stringVar.isalpha()
# 모음: aeiou
num = 0
s = input("문자열을 입력하세요: ")
if s.isalpha():
    newS = s.lower()
    for c in newS:
        for i in "aeiou":
            if c == i:
                num += 1
    print("모음은 %d개, 자음은 %d개입니다." %(num, len(s) - num))
else:
    print("알파벳이 아닌 문자가 포함되어 있습니다.")
