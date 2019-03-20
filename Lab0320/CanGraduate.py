print("140학점 이상 이수, 평점 2.0 이상인 자만 대학을 졸업할 수 있습니다.")
credits = float(input("이수한 학점수르 입력하세요: "))
gpa = float(input("평점을 입력하세요: "))
if credits >= 140 and gpa >= 2.0:
    print("졸업할 수 있습니다!")
else:
    print("졸업이 힘듭니다..")
