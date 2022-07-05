from bisect import bisect_left, bisect_right

n, k = map(int, input().split()) # N과 K를 입력 받기
a = []

for i in range(n):
    a.append(int(input()))


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
	right_index = bisect_right(a, right_value)
	left_index = bisect_left(a, left_value)
	return right_index - left_index
    
if k not in a:
    print(-1)
else:
    # 값이 4인 데이터 개수 출력
    print(count_by_range(a, k, k))

