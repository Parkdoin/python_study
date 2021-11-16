# 숫자맞추기게임
import random
import art

print(art.logo)
print('당신의 이름은 ?')
name = input()

print(f'안녕하세요 {name}님 1에서 20까지 숫자중 하나를 생각합니다.')
secretNumber = random.randint(1,20) # 1부터 20까지의 숫자를 랜덤으로 생성

for count in range(1,7): # 6번의 맞출기회
    guess = int(input())
    
    if guess < secretNumber:
        print('그 숫자보다 큰수')
    elif guess > secretNumber:
        print('그 숫자보다 작은수')
    else:
        break # 맞추면 루프를 빠져나옴
    
if guess == secretNumber:
    print(f'축하합니다. {name}님 {count}번만에 맞췄어요.')
else:
    print(f'툴렸네요. 정답은 {secretNumber}였습니다.')