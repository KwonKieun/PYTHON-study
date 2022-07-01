from itertools import combinations
s, x = input("2자리 이상 정수와 제거할 수의 개수를 입력하세요. : ").split(',')

array = []
for i in range(len(s)):
    array.append(s[i])

result = list(combinations(array, len(array) - int(x))) # 모든 조합 구하기
max_result = 0

for j in range(len(result)):
    if max_result < int(''.join(result[j])):
        max_result = int(''.join(result[j]))

print(max_result)