# 0, 1로 시작하는 피보나치 수이다. N이 주어 졌을때, 피보나치 수를 구하는 프로그램을 작성하시오

import time
import random


# 일반 재귀함수로 피보나치 구현
n = int(input('피보나치 n을 입력 : ')) # 실행 해 본 후 n을 30~50정도로 테스트

start_time = time.time() # 측정 시작

def Fibonacci(num):
	if num == 0:
		return 0
	elif num == 2 or num == 1:
		return 1
	return Fibonacci(num - 2) + Fibonacci(num - 1) # 점화식 표현 중요!

print(Fibonacci(n))

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
