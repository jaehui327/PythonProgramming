# 어떤 요소의 리스트 안에서의 위치를 알려면 index()을 사용한다.
heroes = ["스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨", "조커"]
print(heroes)

index = heroes.index("슈퍼맨")
print(index)

heroes.pop(1)
print(heroes)

heroes.remove("조커")
print(heroes)
