# 도전2 - 소수 - 큰 소수 문자열

import math

def is_prime_number(n):
	li = [1] * (n+1)
	for i in range(2, int(math.sqrt(n))+1):
		if li[i]:
			for j in range(i+1, n+1, i):
				li[j] = 0
	p = [i for i in range(2, n+1) if li[i]]
	return p

while 1:
	s = input()
	max_string = []
    
	if s == '0':
		break
	p = is_prime_number(100000)
	res = 2
	for n in p:
		if str(n) is s:
			res = n
			max_string.append(res)
	print(max_string)
	print(max(max_string))






"""import math
from itertools import combinations


user_input = input("숫자열을 입력하세요. : ")
n_array = []
for i in range(len(user_input)):
    n_array.append(user_input[i])

result = []

for j in range(len(n_array)):
	result += combinations(n_array, len(n_array) - j)

b = []

for r in range(len(result)):
    a = ''.join(result[r])
    b.append(a)
    
print(b)"""

