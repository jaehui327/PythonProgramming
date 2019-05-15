# CSV 파일 분석
# CSV 파일은 split() 메소드를 이용하여 파싱(parsing)될 수 있다.
# open(), readlines(), strip() 메소드를 사용하여서 다음과 같은 CSV 파일에서 데이터를 읽는 프로그램을 작성하여 보자.
# open(): 파일 열기, readlines(): 파일에서 한 줄씩 가져오기
# string.strip(): 문자열 양쪽 공백 제거
fname = 'students.txt'
file = open(fname, "r")

for line in file.readlines():
    line = line.strip()
    print(line)
    words = line.split(",")
    for word in words:
         print(word)
