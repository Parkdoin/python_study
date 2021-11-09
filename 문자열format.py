# f - string
name = '홍길동'
age = 20
print(f'안녕하세요 {name}님 나이가 {age}살 이군요')

# 2. 문자열.format()
number = 20
welcome = '환영합니다'
print('{} 번 손님 {}'.format(number, welcome))

# 예제1
name = input('이름을 입력하세요: ')
color = input('좋아하는 색을 입력하세요: ')
print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name, color))
print(f'안녕하세요. 제 이름은 {name}이고 좋아하는 색상은 {color}입니다.')
print('안녕하세요. 제이름은 %s이고 좋아하는 색상은 %s입니다.'%(name, color))

# 문자열 인덱스 : 문자열의 위치를 의미하는 인덱스
string1 = "abcdefg"
print(string1[2]) # c
print(string1[1:5]) # bcde
print(string1[::-1]) # 역순 gfedcba
# 슬라이싱 [시작:끝:증감], [::증감]

# 인덱스 번호로 값을 가져오는것은 가능하지만 수정은 불가


