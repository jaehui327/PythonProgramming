# 회문 검사하기
# 회문(palindrome)은 앞으로나 읽으나 뒤로 읽으나 동일한 문장이다.
# 예를 들어서 "mom, "civic", "dad"등이 회문의 예이다.
# 사용자로부터 문자열을 입력받고 회문인지를 검사하는 프로그램을 작성하여 보자.
# 출력 결과
# 문자열을 입력하시오: dad
# 회문입니다.
sentence = input("문자열을 입력하시오: ")
length = len(sentence)

if length % 2 == 0:
    mid = length // 2 - 1
    for i in range(0, mid + 1):
        if sentence[i] != sentence[length - i - 1]:
            print("회문이 아닙니다.")
            exit(0)
    print("회문입니다.")
else:
    mid = length // 2
    for i in range(0, mid + 1):
        if sentence[i] != sentence[length - i - 1]:
            print("회문이 아닙니다.")
            exit(0)
    print("회문입니다.")