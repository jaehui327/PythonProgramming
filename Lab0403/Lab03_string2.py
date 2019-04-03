# 문자열을 받아서 모음을 전부 없애는 코드는 다음과 같이 작성할 수 있다.
# 모음: aeiouAEIOU
# 결과값
# 문자열을 입력하시오: kkkoommm
# kkkmmm
newString = ''
s = input("문자열을 입력하세요: ")
for c in s:
    for i in "aeiouAEIOU": # if i not in "aeiouAEIOU": newString += i
        if c == i: c = ''
    newString += c
print(newString)