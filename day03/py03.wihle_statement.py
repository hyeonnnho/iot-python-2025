# while 반복문 : for문을 변경
# while (조건이 참인 동안):
#       구문 안에서 반복

# 1 ~ 10 까지의 수를 합ㄴ산

sum = 0
i = 0
while i <= 10:
    sum += i
    i += 1 # i = i + 1, 같은 의미,  +=, -=m *=, /=
print(f'합은 {sum}')

sum = 0
for j  in range(1, 10+1):
    sum += j
print(f'합은 {sum}')