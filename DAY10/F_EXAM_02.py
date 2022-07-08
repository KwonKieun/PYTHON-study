from bisect import bisect_left, bisect_right
import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(b, left_value, right_value):
	right_index = bisect_right(b, right_value)
	left_index = bisect_left(b, left_value)
	return right_index - left_index

# M(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))


i = 1
for i in range(len(target)):
    # 이진 탐색 수행 결과 출력
    # 값이 target[i]인 데이터 개수 출력
	result = count_by_range(a, target[i], target[i]) # target[i]이 존재한다면 1 반환됨
	if result == 1:
		print("Yes")
	else:
		print("No")