N, X = map(int, input().split())

N_list = list(map(int, input('오름차순으로 정렬된 수열을 입력하시오. : ').split()))

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
   if left_value == right_value and left_value not in a:
      print('-1')
   else: 
      right_index = bisect_right(a, right_value)
      left_index = bisect_left(a, left_value)
      return right_index - left_index
   

print(count_by_range(N_list, X, X))