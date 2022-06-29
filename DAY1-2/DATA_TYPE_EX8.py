# 튜플에 리스트 문자열을 저장하고 출력
# 튜플 () 선언
# 기존 리스트 데이터 받아 튜플로 캐스팅 후 출력

lst = []
while True:
    b = input("문자열을 입력하세요 : ")
    if b == ' ':
        break
    lst.append(b)
a = tuple(lst)
print(a)