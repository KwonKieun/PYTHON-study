# 입력으로 들어오는 모든 수의 평균값 계산하는 함수 작성하기
# 입력 개수는 가변이다. 함수 이름 : avg
# 리스트 활용, for문, append로 데이터 저장
# 전체 합(sum()) / len() 함수 = 평균을 리턴

def avg(*args):
    arr = []
    for i in args:
        arr.append(i) # 매개변수를 각각 추가 저장
        
    temp = 0
    for j in arr:
        temp += j # temp에 합한 결과를 누적
    
    return temp/len(arr) # 평균 계산 리턴

print('입력한 정수의 평균을 출력 : ', avg(5, 10, 5, 10))