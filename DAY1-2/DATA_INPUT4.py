date = input('문자를 입력해주세요, 닷으로 구분 : ').split('.')
print('-'.join(date)) # 문자 '-'로 연결 출력
date.reverse() # 구분된 문자열 역 뒤집기(정렬x)
print(':'.join(date))
print(date[0], date[1]) # 구분된 문자의 내부 인덱스 번호로 출력