# 문자열 분석
# 문자열 안에 있는 문자의 개수, 숫자의 개수, 공백의 개수를 계산하는 프로그램을 작성하여 보자.
# string.isalpha(): 문자 여부 확인
# string.isdigit(): 숫자 여부 확인
# string.isspace(): 공백 여부 확인
# 출력 결과
# 문자열을 입력하시오: A picture is worth a thousand words.
# {'digits':0, 'spaces':6, 'alphas':29}
dic = {'digits':0, 'spaces':0, 'alphas':0}
sentence = input("문자열을 입력하시오: ")
for i in sentence:
    if i.isalpha():
        dic['alphas'] += 1
    if i.isdigit():
        dic['digits'] += 1
    if i.isspace():
        dic['spaces'] += 1
print(dic)
