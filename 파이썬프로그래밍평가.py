# # 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값을 출력하는 프로그램을 작성하라.
# # input은 입력을 받는 파이썬의 함수로 통상 아무것도 지정해주지 않으면 문자열만을 받게 되는데
# # 이처럼 정수형으로 바꿔주는 함수인 int()묶어주면 정수형을 받을 수 있다.
# # 그리고 input()안에 문자열을 넣으면 사용자로부터 입력을 받을때 메시지를 의미한다

# num1 = int(input("정수1: "))
# num2 = int(input("정수2: "))

# print("합은: %s 입니다." % (num1 + num2))


# # 두 개의 숫자를 입력 받은 후 두 숫자의 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/) 결괏값을 출력하라.
# # 파이썬에서 +와 -는 수학과 동일하나 곱과 나눗셈은 프로그래밍 언어에서 *와 /를 사용한다.
# # 나눗셈을 할 때 /는 나눈 몫을 구하는 연산자이고, %는 나눈 나머지를 구하는 연산자이다.
# # f-string으로 print 소수점은 1(한자리)로 정한다
# num1 = int(input("first number: "))
# num2 = int(input("second number: "))

# print(f"add: {num1 + num2}")
# print(f"sub: {num1 - num2}")
# print(f"mul: {num1 * num2}")
# print(f"div: {num1 / num2}")


# # for 문을 중첩하여 구구단을 2단부터 9단까지 가로로 한줄씩 만드시오.
# for i in range(1,10):
#     for j in range(2,10):
#         print(j, 'x', i, '=', j*i, end='\t')
#     print()


# # 블로그 숫자 맞추기 게임 참조
# # 1에서 20까지의 랜덤값 지정  사용자 이름 입력
# # 랜덤값을 맞추는데 6번 미만으로 맞췄을때 잘 맞췄어요 이름님 몇번 만에 맞췄어요 출력
# # 만약 6번 이상일때는 틀렸습니다. 정답은 x 입니다. 출력
# import random
# import art

# print(art.logo)
# print('당신의 이름은 ?')
# name = input()
# print(f'안녕하세요 {name}님 1에서 20까지 숫자중 하나를 생각합니다.')
# secretNumber = random.randint(1,20) # 1부터 20까지의 숫자를 랜덤으로 생성
# for count in range(1,7): # 6번의 맞출기회
#     guess = int(input())
#     if guess < secretNumber:
#         print('그 숫자보다 큰수')
#     elif guess > secretNumber:
#         print('그 숫자보다 작은수')
#     else:
#         break # 맞추면 루프를 빠져나옴
# if guess == secretNumber:
#     print(f'축하합니다. {name}님 {count}번만에 맞췄어요.')
# else:
#     print(f'툴렸네요. 정답은 {secretNumber}였습니다.')


# # 블로그 Ex-1 참조
# # 튜플(3개 이상)을 입력받아서  첫번째 값, 세번째 값, 끝에서 두번째 값을 
# # 튜플로 만들어 리턴하는 함수를 만들어서 실행결과를 표시하라.
# def easy_unpack(elements):
#     return (elements[0], elements[2], elements[-2])  

# if __name__ == '__main__':
#     print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
#     assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
#     assert easy_unpack((6, 3, 7)) == (6, 7, 3)


# # 블로그 Ex-1 참조
# # 패스워드는 길이가 6보다 커야 한다. 이에 맞는 함수를 만들어서 
# # 출력 결과를 표시하라.
# def is_acceptable_password(password):
#     return len(password) > 6
    
# if __name__ == '__main__':
#     print(is_acceptable_password('short'))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False


# # 블로그 Ex-1 참조
# # 정수(int)의 길이를 구하여라. 이에 맞는 함수를 만들어서 
# # 출력 결과를 표시하라.
# def number_length(a):
#     return len(str(a))
# if __name__ == '__main__':
#     print(number_length(10))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert number_length(10) == 2
#     assert number_length(0) == 1
#     assert number_length(4) == 1
#     assert number_length(44) == 2


# # 블로그 Ex-2 참조
# # 리스트 items 와 정수 i를 입력받아서, 만약 i가 items에 있으면 i 앞의 숫자들을 제거하고
# # 리턴하고 없으면 items 전체를 그대로 리턴하는 함수를 작성하고 테스트 하여라.
# def remove_all_before(items, i):
#     # 코드 작성
#     if i in items:
#         return items[items.index(i):]
#     else :
#         return items

# if __name__ == '__main__':
#     print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
    
#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
#     assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
#     assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
#     assert list(remove_all_before([], 0)) == []


# 블로그 Ex-2 참조
# 리스트를 입력받아 첫번째 아이템을 맨 마지막으로 보낸다음 리턴하고, 빈 리스트[] 나 
# [1] 처럼 하나의 값이 있을때는 같은 리스트가 리턴하는 함수를 만들어서
#  출력 결과를 표시하라.
def replace_first(items):
     if len(items) > 1:
        items.append(items.pop(0))
     return items

if __name__ == '__main__':
    print(list(replace_first([1, 2, 3, 4])))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
