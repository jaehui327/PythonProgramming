# 문자열 처리 프로그램
# 리스트는 문자열도 저장할 수 있다.
# 강아지를 많이 키우는 사람을 가정하자.
# 가아지들의 이름을 저장하였다가 출력하는 프로그램을 작성해보자. (엔터키 문자열: "")
puppies = []
i = 0
while(1):
    name = input("강아지의 이름을 입력하세요(종료시에는 엔터키): ")
    if name =="":
        break
    puppies.append(name)
print("강아지들의 이름:")
for puppy in puppies:
    print(puppy, end = ", ")
