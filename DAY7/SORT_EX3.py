# 기본 방식1 (람다 키 사용)

n = int(input())
array = []

for i in range(n):
    a = list(input().split())
    array.append(a)

array2 = sorted(array, key=lambda x : x[0])  # 정렬하는 키 기준이 리스트의 첫번째 값

for e in array2:
  	print(' '.join(e))
    
# for i in array2:
#     print(i[0], i[1])