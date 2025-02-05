# for문 : 프로그래밍의 꽃
# 반복을 처리할 때 사용
# for 변수 in 반복할 값:
#   구문 안으로 ...

# 아래와 같이 출력되는 프로그램을 작성하시오
'''
*
**
***
****
'''

# range() 범위를 생성 클래스
# 마지막 수 : max -1
# range(8) -> range(0,8)
# range(init, max, add)
# print(range(8))

# for i in [0, 1, 2, 3, 4, 5, 6, 7]: # 이 조건이 참인 동안 반복...
# for i in range(0, 8, 2):
#     print(i)

# number = int(input('최대 별 수 : '))
# for i in range(1, number + 1):
#     print('*'* i)

# 구구단(2단 부터 2*9 ~ 9*9)
# 요구사항1 - 한 줄에 각 단씩 나오도록
# 요구사항2 - 모든 줄에 칸을 맞춤
# 요구사항3 - 단 시작을 표시
for x in range(2,10):
    # if x == 8: break # 8단 부터 
    if x == 8: continue # 8단만 뺌 
    print(f'{x}단 시작!')
    for y in range(1, 10):
        # if y == 8: break
        print(f'{x} * {y} = {x * y:2d}', end= '   ')
    print() #한 줄 내리기
print('구구단 종료 \n\n')

## 반복문을 빠져나올 때 : break
## 반복문에서 특정 조건을 지나칠 때 : contiune


