# 일회용 패스워드 생성기를 이용하여 3개의 패스워드를 생성하여 출력하는 프로그램을 작성해보자.
# (알파벳과 소문자와 숫자만 사용)
import random

def getPass():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""

    for i in range(6):
        index = random.randrange(len(alphabet))
        password += alphabet[index]
    return password

print(getPass())
print(getPass())
print(getPass())