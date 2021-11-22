# 리스트는 순서가 있고 수정 가능한 자료구조이다. 값이 중복가능

# 리터럴로 만들기
numbers = [1,2,3,4,5]
fruits = ['사과', '오렌지', '포도', '배']

# 값을 가져오기
print(numbers[0])
print(fruits[0])

# 길이(length) 구하기
print(len(numbers))
print(len(fruits))

# 값 추가하기 append
fruits.append('망고') # 맨 뒤에 추가
print(fruits)

# 제거하기 remove
fruits.remove('포도') # 포도 제거
print(fruits)

# 인덱스로 특정 위치에 입력 insert
fruits.insert(2, '딸기') # 2번째 위치에 딸기 추가
print(fruits)

# 특정 인덱스의 값을 제거 pop
fruits.pop(3) # 3번째 위치의 값 제거
print(fruits)

# 리스트를 거꾸로 리버스 reverse
fruits.reverse()
print(fruits)

# 정렬 리스트(값의 순서대로) sort
fruits.sort()
print(fruits)