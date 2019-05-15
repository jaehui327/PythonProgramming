# 머리 글자어 만들기
# 머리 글자어(acronym은 NATO(North Atlantic Treaty Organization)처럼
# 각 단어의 첫글자를 모아서 만든 문자열이다.
# 사용자가 문장을 입력하면 해당되는 머리 글자어를 출력하는 프로그램을 작성하여 보자.
# 출력 결과
# 문자열을 입력하시오: North Atlantic Treaty Organization
# NATO
sentence = input("문자열을 입력하시오: ")
sentence.upper()
x = sentence.split()
for word in x:
    print(word[0], end="")