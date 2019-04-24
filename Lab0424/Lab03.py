# 성적 처리 프로그램
# 학생들의 성적을 처리하는 프로글매을 완성시켜보자.
# 사용자로부터 성적을 입력받아서 리스트에 저장한다.
# 성적의 평균을 구하고 80점 이상 성적을 받은 학생의 숫자를 계산하여 출력해보자.
# 5명
scores = []
sum = 0
high80 = 0
studentNum = int(input("몇 명의 학생 점수를 입력할 건가요? "))
for i in range(0, studentNum):
    scores.append(int(input("성적을 입력하세요: ")))
    sum += scores[i]
    if scores[i] >= 80:
        high80 += 1
average = sum / studentNum
print("성적 평균은 %.1f입니다." %(average))
print("80점 이상 성적을 받은 학생은 %d명입니다." %high80)
