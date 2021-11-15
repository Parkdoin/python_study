# # while 반복문
# while True:
#     print('무한반복')

# count = 0
# while count < 3:
#     print('횟수 :', count)
#     count += 1

# name = ''
# while name != '펭수':
#     name = input('펭수를 입력해 주세요: ')
    
# print('thank you')

# hit = 0
# while hit < 10:
#     hit += 1
#     if hit % 2 == 0: # 짝수일때 아래코드는 실행하지 않고 다시 조건으로 돌아감
#         continue        
#     print(f'나무를 {hit}번 찍었습니다.')
#     if hit == 5:
#         break # 조건으로 빠져나옴

# []는 파이썬 리스트 타입, 반복문 for는 리스트를 순회하며 코드블록을 실행하는 것
# for n in [1,2,3]:
#     print(n)

# for s in ['다람쥐','펭귄','아나콘다','하이에나']:
#     print(s)
    
# for c in '홍길동님': # 문자열을 순회하며 코드블록을 실행하는 것
#     print(c)
    
# for반복문과 자주쓰는 함수 range(시작, 끝, 증가값) 리턴값은 시작부터 끝까지 증가값으로 순회하는 순서를 리턴한다.
# for n in range(3): # 0,1,2
#     print(n)
    
# # 1부터 100까지 합
# total = 0
# for x in range(1,101):
#     total += x

# print("1에서 100까지 더한값: ", total)

# 구구단 2단
# for i in range(1,10):
#     print(f'2 x {i} = {2*i}')
    
# 예제1 구구단
for i in range(2,10):
    print( )
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}', end='  ')
    