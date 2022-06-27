a = input()
print(a, 3 * ("\n"))
print(a, a, a)

b, c = input("문자 2개를 입력해주세요 : ").split() # 공백 기준 분리
print(b + c + "\n")
print(b, "\n" + c)

d, e = input("문자 2개를 입력해주세요, 콤마 구분 : ").split(',')
print(d, e)

f, g = input('문자 2개를 입력해주세요, 콤마 구분, 1개 제한 : ').split(',', 0) # 문자 2개 입력, 콤마 기준 분리, 1개 제한, 입력에 메시지 삽입
print(f, g, sep=",") # , 로 구분하여 출력