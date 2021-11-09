"""
# 여러개의 변수를 동시에 초기화
a, b, c = 1, 2, 3
print(a, b, c)
print(a)
print(b)
print(c)

# 예제2
x = 10
print(x)

# 예제3
x,y,z = 1,2,3
print(x)
print(y)
print(z)

# 예제4
x,y,z = 1,1.1,'홍길동'
print(type(x))
print(type(y))
print(type(z))

# 예제5
a = input('a : ')
b = input('b : ')
print('a :', b)
print('b :', a)
"""

# 문자열

# 긴 문자열은 따옴표 3개(''', """")를 사용하여 감싸준다.
var3 = '''
'따옴표' 3개는
끝나는 "문장"까지
모두를 문자열로 처리
--------------------------------
'''
# print(var3)

# # 문자열(+연산자)
# 성 = '홍'
# 이름 = '길동'
# Name = 성 +' ' + 이름
# print(Name)

# # 타입 변환 : str(), int(), float()
# print(type(float(int(str(100)))))

# 예제1
print('''
   It\'s \"kind of\" sunny 
Have a nice Day!
''')

# 예제2
string1 = '''
다스베이더가 말했다.
\"내가 니 애비다!\"
그 말을 들은 루크는 \'깜짝\'놀랐다.
'''
print(string1)

# 예제3
print('밴드 이름 만들기 프로그램에 환영합니다.')
city = input('태어난 도시가 어딘가요?\n')
petName = input('애완동물의 이름은?\n')
print('당신의 밴드 이름은', city, petName)
