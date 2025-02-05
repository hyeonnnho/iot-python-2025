# 파일 입출력
# 파일 오픈, 읽고, 쓰고, 닫음
# 파일 경로 : 파일이 컴퓨터 상에 들어있는 위치

# 경로 구분자 \ / 다 사용 가능
# mode : r(읽기), w(쓰기), a(추가), ...
# encoding : 한글만(enc-kr, cp949), 국제어(utf-8)
## 상대경로 - 경로를 특수문자로 생략하는 법
# . : 현재 자기 폴더 위치
# .. : 자신의 부모 폴더 위치
# f = open('./day03/text.txt', mode='w', encoding='utf-8')
# f = open('../text3.txt', mode='w', encoding='utf-8')
## 절대경로 - 드라이브부터 모든 경로를 다 작성하는 방법
# f = open('C:/Source/iot-python-2025/day03/text2.txt', mode='w', encoding='utf-8')
# \를 문자열에 표현하고 싶다면
# f = open('C:\\Source\\iot-python-2025\\day03\\text4.txt', mode='w', encoding='utf-8')

# f.write('파일 쓰기 시작!\n')
# f.write('두번째 줄 작성 합니다.\n')
# f.write('\n)

# print('파일 쓰기 완료')

r = open('./day03/text.txt', mode='r', encoding='utf-8')
while True:
    line = r.readline() # 한 줄씩 읽음
    if not line: # 한 줄을 읽은 값이 None이면 
        break # while문을 탈출하라
    # print(line, end = '')
    print(line.replace("\n",""))
r.close()