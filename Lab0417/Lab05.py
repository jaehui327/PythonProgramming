# 계산기 프로그램을 만들어보자.
# (실행은 0, 종료는 1)
# 실행, 종료 결정 시 다른 문자가 들어가도 종료가 되지 않게 한다.
# +, -. *, / 연산이 가능하게 프로그램 만들기
# 다른 문자가 들어가면 실행이 되지 않는다.
def calculator(first, operator, second):
    if operator == '+':
        print("덧셈 결과는 %.1f입니다." %(first + second))
    elif operator == '-':
        print("뺄셈 결과는 %.1f입니다." % (first - second))
    elif operator == '*':
        print("곱셈 결과는 %.1f입니다." % (first * second))
    elif operator == '/':
        print("나눗셈 결과는 %.1f입니다." % (first / second))
    else:
        print("연산자 입력이 잘못되었습니다.")
option = 0
first = 0
operator = ''
second = 0
while(1):
    print("====================================")
    print("계산기 프로그램 만들기")
    print("0. 계산기 실행하기")
    print("1. 종료하기")
    print("====================================")
    option = int(input("실행: "))
    if option == 1:
        print("프로그램 종료")
        break
    first = int(input("첫번째 수를 입력해주세요: "))
    operator = input("계산 연산자를 입력해주세요(+, -, *, /): ")
    second = int(input("두번째 수를 입력해주세요: "))
    calculator(first, operator, second)
