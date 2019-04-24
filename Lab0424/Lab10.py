# 연락처 관리 프로그램 (contacts.py)
# 파이썬을 이용하여 연락처를 관리하는 프로그램을 작성하여 보자.
# 연락처 관리 프로그램은 다음과 같은 메뉴를 가져야 한다.
names = []
op = 0
while(1):
    print("--------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    op = int(input("메뉴를 선택하세요: "))
    if op == 1:
        print(names)
    elif op == 2:
        name = input("이름을 입력하세요: ")
        names.append(name)
    elif op == 3:
        name = input("삭제할 이름을 입력하세요: ")
        if name in names:
            names.remove(name)
    elif op == 4:
        name = input("변경하고 싶은 이름을 입력하세요: ")
        if name in names:
            changeName = input("새로운 이름을 입력하세요: ")
            index = names.index(name)
            names[index] = changeName
        else:
            print("이름이 발견되지 않았음")
    elif op == 9:
        break
    print("--------------------")
