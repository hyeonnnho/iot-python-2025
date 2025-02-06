# 예외처리
## 오류, Error, Fault,
## 1. Error(문법적 오류) : 코딩 중 빨간 밑줄
##    오류표시가 안나는 코딩을 잘못한 오류 포함 mul(7, 6) -> 42 예상, but 13
## 2. Exception(실행 중 발생 예외) : 문법적 오류 수정 후 실행 중 비정상 종료
## 파이썬은 Error와 Exception 둘 다 Error
## 에디터 상에 오류표시가 나면 Error
## 실행 중에 발생 시 Exception

numbers = list(range(1,11))
for i in numbers:
    # print(i)
    pass

def mul(a,b):
    return a * b
def div(a,b):
    return a / b

print('계산 시작')
while True:
    op = input('계산할 연산을 입력(*, /, q)')
    if op == 'q': # 종료 조건
        break
    
    elif op == '*': # 곱하기
        x, y = input('곱할 수 입력 >>').split()
        x = int(x)
        y = int(y)
        print(f'{x} * {y} = {mul(x, y)}')
        
    elif op == '/': # 나누기
        x, y = input('나눌 수 입력 >>').split()
        x = int(x)
        y = int(y)
        print(f'{x} / {y} = {div(x,y)}')
    
    else:
        print('정확하게 입력 바랍니다.')