# 화면 입출력

print('출력입니다')

number = input('만나이를 입력하세요 >') # 입력방법
# 입력되는 값, 출력되는 값 모두 문자열!
number = int(number) # str -> int
print(type(number))
print("현재나이는", number + 1) # 여러 값을 같이 출력하려면 ,로 구분

x, y = input('합산할 두 수를 입력하세요 > ').split() # 기본으로 공백으로 잘라줘
print(x + y)
x = int(x)
y = int(y)
print(x + y)
