# N종류의 동전을 사용할 수 있다. 가격의 합 K를 만드는 동전 개수의 최소값을 출력하시오

n, k = map(int, input("화폐 개수와 돈의 가격 입력 : ").split())
Ai = []
for i in range(n):
    a = int(input("동전 가격을 개수만큼 입력 : "))
    Ai.append(a)
Ai.sort(reverse = True)

count = 0
for coin in Ai:
    count += k // coin
    k %= coin
    
print('동전의 거스름돈 최소 개수는 :', count)