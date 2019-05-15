# 단어 카운터
# 사용자가 지정하는 파일을 읽어서 파일에 저장된 각각의 단어가 몇 번이나 나오는지를 계산하는 프로그램을 작성하여 보자.
# 출력 결과
# 파일 이름: proverbs.txt
# {'a':1, 'done.':1 ... }
# 파일 읽기
fname = 'proverbs.txt'
file = open(fname, "r")

# dictionary 생성
count_dict = dict()

# 파일의 모든 줄에 대하여 반복한다.
for line in file:
    # print(line)
    lineWords = line.split()
    for word in lineWords:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

print(count_dict)
