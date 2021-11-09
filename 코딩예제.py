# 예제1
number = input('두 자리 숫자를 입력:\n')
print('두 숫자의 합은 %d' % (int(number[0]) + int(number[1])))

# 예제2
height = input('키를 미터 단위로 입력하세요 : ')
weight = input('몸무게를 킬로 단위 입력하세요 : ')
print('당신의 bmi는 {:.2f} 입니다.' .format((float(weight)) / (float(height)**2)))