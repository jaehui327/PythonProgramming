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