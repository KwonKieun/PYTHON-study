n = int(input('10진수를 문자로 출력 : '))
print(chr(n)) #10진수를 문자로 캐스팅 출력
print(ord(input('a~z 문자 위치 출력 : '))) #문자를 숫자(아스키코드) 출력

print('%x'%int(input('10진수를 유니코드로 출력 :'))) # 10진 정수 --> 유니코드 출력
print('%x'.upper()%int(input('10진수를 대문자로 출력 : '))) # 10진 정수 --> 유니코드(대문자) 출력

f = int(input('정수의 부호를 변환 : '))
print(-f) # 부호 변환 출력

c=input('입력 문자의 다음 문자 출력 : ')
c2=ord(c)+1 # 아스키 코드 값을 1 증가
print(chr(c2))# 10진 정수 --> 문자 출력