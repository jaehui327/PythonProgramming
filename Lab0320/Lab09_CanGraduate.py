# 졸업 학점 검사하기
# 어떤 대학교를 졸업하려면 적어도 140학점을 이수해야 하고 평점이 2.0은 되어야 한다고 하자.
# 이것을 파이썬 프로그램으로 검사해보자.
# 사용자에게 이수학점수와 평점을 물어보고 졸업 가능 여부를 출력하는 프로그램을 작성해보자.
print("140학점 이상 이수, 평점 2.0 이상인 자만 대학을 졸업할 수 있습니다.")
credits = float(input("이수한 학점수르 입력하세요: "))
gpa = float(input("평점을 입력하세요: "))
if credits >= 140 and gpa >= 2.0:
    print("졸업할 수 있습니다!")
else:
    print("졸업이 힘듭니다..")

