# 파일 읽기
fname = 'proverbs.txt'
file = open(fname, "r")

# 파일의 모든 줄에 대하여 반복한다.
for line in file:
    # print(line)
    lineWords = line.split()
    
    print(lineWords)