# 줄임말 만들기
# 사용자에게 단어 3개를 입력받아서 약자(acronym: 몇 개 단어의 머리글자로 된 말)을 만들어 보자.
# 예를 들어서 'OST'도 Original Sound Track의 약자이다.
# 이 예제는 소스 파일로 작성하여 실행해보자.
first = input("첫 번째 단어를 입력해주세요: ")
second = input("두 번째 단어를 입력해주세요: ")
third = input("세 번째 단어를 입력해주세요: ")
#string = [first[0], second[0], third[0]]
#print(string)

# print(first[0], second[0], third[0])

acronym = first[0] + second[0] + third[0]
print(acronym)