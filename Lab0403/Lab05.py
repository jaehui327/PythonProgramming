# 인터넷 뱅킹을 사용하다 보면 계좌번호를 입력할 때, "312-02-1234567"과 같이 "-"을 사용하면 안된다는 경고를 받는다.
# 사용자로부터 "-"가 포함된 계좌번호를 받아서 "-"을 삭제한 문자열을 만들어보자.
s = input("계좌번호를 입력하세요: ")
newS = ""
for c in s:
    if c != "-":
        newS += c
print(newS)
