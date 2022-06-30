"""s = list(input())

list_atoz = [-1 for i in range(26)]

print(list_atoz)

for j in range(ord(s)):
    a = s[j]
    print(a)"""
        

user_input = input('100글자 이내 소문자 문자열 1개 입력: ')
check = [-1]*26  # 26개 크기 리스트 생성 -1로 초기화, check = [-1 for _ in range(26)] 가능

for i in range(len(user_input)):  # 입력한 문자의 길이까지, ohmygod 예) 길이 7
    index = ord(user_input[i]) - 97  # 소문자 o, 111-97
    if check[index] == -1:  # 14번째 인덱스는 -1이므로
        check[index] = i  # 0 입력
    # 이후 반복문 돌면서 각 문자를 1씩 증가된 위치로 표시
    
print('입력된 소문자의 위치를 표시: ', *check)