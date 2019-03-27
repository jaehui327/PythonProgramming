# 화씨온도 - 섭씨온도 변환 테이블 출력
f = 0
for f in range(0, 101, 10):
    c = (f - 32) * 5 / 9
    print("%d -> %.2f" %(f, round(c, 2)))
