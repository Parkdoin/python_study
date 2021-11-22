# try/except

def div10(n): # 입력값에 10을 나눠서 리턴하는 함수
    try:
        return 10/n
    except ZeroDivisionError:
        return '에러 : 0으로 나눌 수 없음.'
    
print(div10(2))    
print(div10(0))  # 0으로 나누면 예외가 발생하므로 0을 리턴한다.  
print(div10(5))    


