# 1년의 각 달의 일수를 출력하는 프로그램을 작성해보자.
# 즉 특정 달이 입력되면 그 달의 일수를 출력한다.
# 여러 가지 방법으로 작성할 수 있겠으나, 여기서는 if-else문을 사용해보자.
month = int(input("월을 입력하세요: "))
if month == 2:
    print("월의 날수는 29일")
elif month == 4 or month == 6 or month == 10:
    print("월의 날수는 30일")
else:
    print("월의 날수는 31일")