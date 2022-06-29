# 정수(1~100) 1개를 입력 받아 1부터 그 수까지 짝수의 합 출력
a = int(input("정수(1~100)를 입력하시오 : "))
i = 1
summ = 0
while i <= a:
    summ += i
    i += 1
print(summ)

# 영문 소문자 q가 입력될 때까지 입력 문자를 무한 출력하시오.
i = input("문자를 입력하시오. : ")
while True:
    i = input("문자를 입력하시오. : ")
    if i == 'q':
        print("q가 입력되었습니다.")
        break
