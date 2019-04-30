# 아이디를 입력받아서 등록된 아이디인지를 검사하는 프로그램을 작성해보자.
# 등록된 아이디를 리스트(list)에 저장하도록 한다.
# 아이디가 일치하면 패스워드를 물어본다.
userList = ['김재희', '이성현']
passwd = "12345678"
id = input("아이디를 입력하세요: ")
if id in userList:
    PW = input("비밀번호를 입력하세요: ")
    if PW == passwd:
        print("환영합니다.")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("등록되지 않은 아이디입니다.")