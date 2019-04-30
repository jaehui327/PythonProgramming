# 별 도착 시간 계산
# 지구에서 가장 까까운 별은 프록시마 켄타우리(Proxima Centauri) 별이라고 한다.
# 프록시마 켄타우리는 지구로부터 (40 x 10^12) 떨어져 있다고 한다.
# 빛의 속도 (3 x10^6 m/s)로 프록시마 켄타우리까지 간다면
# 시간이 얼마나 걸리는지 직접 계산해보기로 하자.
star = 40 * 10 ** 12
second = star / 3 * 10 ** 5
year = second / (60 * 60 * 24 * 365 * 3 * 10 ** 8)
print("지구에서 켄타우리 별까지 ", year, "광년이 걸립니다.")

