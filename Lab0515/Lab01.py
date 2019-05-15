# 영한 사전 만들기
# 우리는 영한 사전을 구현하여 보자.
# 어떻게 하면 좋은가?
# 공백 딕셔너리를 생성하고 여기에 영어 단어를 키로 하고 설명을 값으로 하여 저장하면 될 것이다.
# one, two, three
# 출력 결과
# 단어를 입력하시오: one
# 하나
dic = {'one':'하나','two':'둘', 'three':'셋'}
word = input("단어를 입력하시오: ")
# if word in dic:
#   value = dic['one']
#   print(value)
# else:
#   print("없음")
print(dic.get(word, "없음"))