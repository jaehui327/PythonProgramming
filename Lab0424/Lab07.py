# 리스트 일치 검사
# 우리는 비교 연산자 ==, !=, >, <를 사용해서 2개의 리스트를 비교할 수 있다.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
ans1 = (list1 == list2)
print(ans1)

list1 = [3, 4, 5]
list2 = [4, 5, 6]
ans2 = (list1 <= list2)
print(ans2)

# 리스트 정렬하기
# 1. 리스트 객체의 sort() 메소드를 사용하는 방법
a = [3, 2, 1, 5, 4]
print(a)
a.sort()
print(a)
# 2. sorted() 내장 함수를 사용하는 방법
a = [3, 2, 1, 5, 4]
print(a)
b = sorted(a)
print(b)