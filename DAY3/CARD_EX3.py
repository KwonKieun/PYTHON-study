"""n, m = map(int, input("행과 열을 입력하세요. : ").split())
array=[]
for i in range(n):
    a = list(map(int, input().split()))
    array.append(a)

a = 0

for j in range(array):
    if a < min(array[j]):
        a += min(array[j])
    
print(a)"""


n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)