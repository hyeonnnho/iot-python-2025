import os
from Movie import Movie


VERSION = 0.5

def clearScreen(): # os 에 특화된 팁
    command = 'clear'
    if os.name  in('nt', 'dos'):
        command = 'cls'
    os.system(command)

# 메인에서 가장 먼저 실행되는 함수
def run():
    # movie = Movie('어벤져스: 인피니티 워', 2018, '디즈니', 8.6)
    # print(movie)
    # set_movie()
    clearScreen() # 최초의 화면 클리어
    lst_movie = [] # 영화 리스트
    load_movie(lst_movie)

    while True:
        sel_menu = set_menu()
        if sel_menu == 1:
            # print('영화 입력')
            movie = set_movie()
            lst_movie.append(movie)
        elif sel_menu == 2:
            print('영화 출력')
            get_movie(lst_movie)
        elif sel_menu == 3:
            print('영화 검색')
            title = input('검색할 영화명 입력 >> ')
            search_movie(lst_movie, title) 
        elif sel_menu == 4:
            print('영화 삭제')
            title = input('삭제할 영화명 입력 >> ')
            del_movie(lst_movie, title) 
        elif sel_menu == 5:
            # print('앱 종료')
            # 종료직전 DB생성하고 완료
            save_movie(lst_movie)
            break # 반복문 탈출
        else:
            pass # 아무 것도 하지 않음  

        input() # 입력대기 : 엔터치면 넘어감
        clearScreen()  # 메뉴 기능이 완료되면 화면클리어                               

def set_movie():
    title, year, company, rate = input('영화입력[제목|개봉년|제작사|평점 순] > ').split('|') # 입력 중 발생하는 예외
    # print(title, year, company, rate)
    year = int(year) # 년도는 정수로
    rate = float(rate) # 평점은 실수로
    movie = Movie(title=title, year=year, company=company, rate= rate) # 데이터형 예외
    return movie

def get_movie(items: list): # items 변수 list타입 지정
    for item in items:
        print(item) # Movie 객체

def search_movie(items: list, title: str):
    for item in items: # item이 Movie 클래스인지 알 수 없음
        if item.isNameContain(title): # 오타 발생 위험
            print(item)

def del_movie(items: list, title: str):
    for i, item in enumerate(items): 
            if item.isNameExist(title):
                del items[i] # 인덱스로 리스트에 요소 하나를 삭제
            # del(item[int(input('숫자'))])

# 폴더에 파일로 영화 리스트 저장
def save_movie(items: list):
    f = open('movie_db.txt', encoding='utf-8', mode='w') # 파일 쓰기로 오픈
    for item in items:
        f.write(f'{item.getTitle()}|')
        f.write(f'{item.getYear()}|')
        f.write(f'{item.getCompany()}|')
        f.write(f'{item.getRate()}\n')
    f.close()

def load_movie(items: list):
    f = open('movie_db.txt', encoding='utf-8', mode='r')
    while True:
        line = f.readline().replace('\n','') # 어벤져스:엔드게임|2018|디즈니|8.6
        if not line: break # 무한루프 빠져나가는 조건
        lines = line.split('|') # 구분자로 잘라서 4개의 요소의 리스트 생성
        title = lines[0]
        year = int(lines[1])
        company = lines[2]
        rate = float(lines[3]) # '8.6\n'
        movie = Movie(title, year, company, rate)
        items.append(movie)
    f.close()

def set_menu():
    str_menu = (f'내영화 앱 v{VERSION}\n'
                '1. 영화 입력\n'
                '2. 영화 출력\n'
                '3. 영화 검색\n'
                '4. 영화 삭제\n'
                '5. 앱 종료\n')
    print(str_menu)
    try:
        sel_menu = int(input('메뉴 번호입력: ')) # 예외있음
    except Exception as e :
        sel_menu = 0
    return sel_menu

if __name__ == '__main__':
    # print('내 영화 앱 시작')
    run()


print('프로그램 종료')