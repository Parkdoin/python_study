# 함수 만들기
# # 함수 만들기
# def hello(): # 함수 선언
#     print('하이!')
#     print('안녕!')
#     print('니 하오!')
    
# hello() # 함수 호출


# # 매개변수(parameter, 입력값) 있는 함수
# def hello(name):
#     print('하이! '+name)
    
# hello('길동')
# hello('펭수')


# # 매개변수 리턴값 있는 함수
# def add10(n):
#     return n+10

# print(add10(10))


# # 예제 1
# def is_odd(num):
#     if num % 2 == 1:
#         print('홀수')
#     else:
#         print('짝수')
    
# is_odd(11)
# is_odd(12)

# 예제 2
def foo(*arg): # * 은 여러개의 매개변수를 받는다는 의미
    avg = sum(arg) / len(arg)
    print(avg)
    
foo(1,2,3,4,5)
foo(1,2,3,4,5,6,7,8,9,10)
foo(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
