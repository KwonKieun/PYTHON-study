"""user_input = list(input())
small = ['a', 'e', 'i', 'o', 'u']
a = []

for i in range(len(user_input)):
    if user_input[i] in small:
        a = user_input[i]
        i = i + 3
    else:
        a = user_input[i]
        i += 1

print(''.join(a))"""


data = input('암호화된 문장을 공백으로 구분 입력: ')
value = ['a', 'e', 'i', 'o', 'u']
number = 0

while number < len(data):  # 입력된 문장의 길이까지
    print(data[number], end='')  # 한글자씩 출력한다. 공백 구분
    if data[number] in value:  # 모음에 해당되는 문자이면
        number += 2  # 추가된 문자를 건너뛴다. g, 모음 모두 2개
    number += 1  # 다음 문자를 검사 진행