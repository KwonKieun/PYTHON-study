from bisect import bisect_left, bisect_right
import sys
import time
import os
import psutil
from random import randint

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기

N = 2250000
array = []
for _ in range(N):
# 1부터 N 사이의 랜덤한 정수
	array.append(randint(1, N))
array.sort()

# M(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
M = 30
target = []
for _ in range(M):
# 1부터 N 사이의 랜덤한 정수
	target.append(randint(1, M))


start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가



# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(b, left_value, right_value):
	right_index = bisect_right(b, right_value)
	left_index = bisect_left(b, left_value)
	return right_index - left_index



i = 1
for i in range(len(target)):
    # 이진 탐색 수행 결과 출력
    # 값이 target[i]인 데이터 개수 출력
	count_by_range(array, target[i], target[i]) # target[i]이 존재한다면 1 반환됨
        
        
end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력