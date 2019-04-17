# 점수의 평균을 구해보자. (점수는 0과 100점 사이, 종료는 음수)
# 100점을 넘는 인원은 제외
# 음수를 입력하면 입력 종료 및 총 인원과 평균, 최고, 최저 점수 출력
scorePre = 0
score = 0
sum = 0
num = 0
maxScore = 0
minScore = 0
while(1):
    scorePre = score
    score = int(input("점수를 입력해주세요 (종료는 음수입력): "))
    if score < 0:
        break
    elif score > 100:
        print("점수가 100점을 초과하였습니다.")
        score = scorePre
    else:
        sum += score
        num += 1
        maxScore = max(scorePre, score)
        minScore = min(scorePre, score)
print("종료되었습니다.")

print("총 %d명의 전체 평균은 %.1f입니다." %(num, sum / num))
print("최고점수는 %d입니다." %maxScore)
print("최저점수는 %d입니다." %minScore)