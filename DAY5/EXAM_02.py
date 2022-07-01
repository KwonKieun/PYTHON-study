checkNo = '234567892345' # 가중치
rrn = [s for s in input('주민등록번호를 입력하세요.(\'-\' 포함) : ').replace('-', '')]

total = 0 # 주민등록번호 * 가중치 의 합을 담을 변수
for i in range(12):
    total += int(rrn[i]) * int(checkNo[i])  # 주민등록번호와 해당 가중치를 곱하여 모두 합한다.
 
result = (11 - total % 11) % 10 # 합한 값을 11로 나눈 뒤 나온 나머지를 다시 10으로 나누어 그 나머지를 구한다.
 
if str(result) == rrn[12]: # 그 나머지와 주민등록번호 마지막 번호가 같은지 판단한다.
    print('올바른 주민등록번호입니다.')
        

    Y = rrn[0]+rrn[1]
    M = rrn[2]+rrn[3]
    D = rrn[4]+rrn[5]

    if rrn[6] == '1' or rrn[6] == '2':
        print("생년월일 : 19{0}년 {1}월 {2}일".format(Y, M, D))
        if rrn[6] == '1':
            print("성별 : 남성")
        else:
            print("성별 : 여성")
    else:
        print("생년월일 : 20{0}년 {1}월 {2}일".format(Y, M, D))
        if rrn[6] == '3':
            print("성별 : 남성")
        else:
            print("성별 : 여성")

    if int(rrn[7]+rrn[8]) <= 8:    # 일부만 표기하였음
        print("거주지 : 서울특별시")
    elif int(rrn[7]+rrn[8]) <= 12:
        print("거주지 : 부산광역시")
    elif int(rrn[7]+rrn[8]) <= 15:
        print("거주지 : 인천광역시")
    elif int(rrn[7]+rrn[8]) <= 25:
        print("거주지 : 경기도")

else:
    print('주민등록번호 에러!')