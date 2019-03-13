# 등산 시간 계산
from math import *
time = (10 / 20 + 5 / 10 + 5 / 30 + 8 / 20) * 60
hour = int(time / 60)
minute = int(time - (hour * 60))
print("총 걸리는 시간은 ", hour, "시간 ", minute, "분 입니다.")
