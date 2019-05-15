# 축약어 풀어쓰기
# 현대인들은 축약어를 많이 사용한다.
# 예를 들어서 "B4(Before)" "TX(Thanks)" "BBL(Be Back Later)" "BCNU(Be Seeing You)" "HAND(Have A Nice Day)"
# 와 같은 축약어들이 있다.
# 축약어를 풀어서 일반적인 문장으로 변환하는 프로그램을 작성하여 보자.
# 출력 결과
# 번역할 문장을 입력하시오: TX Mr. Park!
# Thanks Mr.Park!

dic = {"B4":"Before", "TX":"Thanks", "BBL":"Be Back Later", "BCNU":"Be Seeing You", "HAND":"Have A Nice Day"}
sentence = input("번역할 문장을 입력하시오: ")

split_word = sentence.split()

for word in split_word:
    if word in dic:
        print(dic.get(word), end=" ")
    else:
        print(word, end="")

