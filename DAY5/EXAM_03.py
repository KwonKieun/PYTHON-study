import random

input_data = input('나이트의 위치 a~h, 1~8 입력 하기 : ') # 현재 나이트의 위치 입력받기, a1
row = int(input_data[1]) # 정수형 입력 받음, 1
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 문자열을 아스키 코드로 변환, a

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] 
result = 0 # 이동 횟수 초기화
avoid = 0 # 회피 횟수 초기화

# 현재 나이트의 위치를 제외한 좌표에 함정 랜덤 6개 생성
traps = []
for i in range(6):
    a = (random.randrange(1, 9), random.randrange(1, 9))
    traps.append(a)
    
print(traps)
    
b = []
for step in steps:
    next_row = row + step[0] # 이동하고자 하는 위치 확인
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        b.append((next_row, next_column))
        # 해당 위치로 이동이 가능하다면 카운트 증가
        # 이동하고자 하는 위치에 함정이 있으면 회피 카운트(avoid) 증가

for i in b:
    if i in traps:
        avoid += 1
    else:
        result += 1

print('{0}번 이동할 수 있습니다. (함정 {1}회 회피!)'.format(result, avoid))