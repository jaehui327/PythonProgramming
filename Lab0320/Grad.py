print("10살 이상, 키 165cm 이상만 놀이 기구를 탈 수 있습니다.")
age = int(input("나이를 입력하세요: "))
height = int(input("키를 입력하세요: "))
if ((age >= 10) and (height > 165)):
    print("놀이 기구를 탈 수 있습니다.")
else:
    print("놀이 기구를 탈 수 없습니다.")
