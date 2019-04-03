# 사용자로부터 임의의 개수의 성저긍ㄹ 받아서 평균을 계산한 후에 출력하는 프로그램을 작성하여 보자.
# 센티널로는 음수의 값을 사용하자
sum = 0
i = 0
score = 0
print("종료하려면 음수를 입력하세요.")
while True:
    score = int(input("성적을 입력하세요: "))
    if score < 0:
        break
    sum += score
    i += 1
print("성적의 평균은 %f입니다." %(sum / i))
