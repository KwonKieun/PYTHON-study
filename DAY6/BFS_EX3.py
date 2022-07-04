from collections import deque # 데큐 연동

n = int(input('단지의 크기 N를 입력 : ')) # 단지 크기 입력
arr = [list(map(int,input('단지 지도 세부 정보를 입력 : '))) for _ in range(n)] # 단지 세부 정보 입력
cnt=0 # 단지안에 속하는 집의 수
cnt_arr=list() # 큐가 끝날때 최종 cnt를 담아줄 배열값

dx = [-1, 0, 1, 0] # 4가지방향 정의
dy = [0, 1, 0, -1]

q = deque() # 큐 선언
              
for i in range(n): # 반복문 시작
    for j in range(n):
        if arr[i][j]==1:
            q.append((i, j)) # 초기 방문 노드 큐에 추가
            arr[i][j]=0
            cnt=1
            while q: # 큐가 존재하는 동안 루프 동작
                x,y=q.popleft() # 큐의 현재 노드를 꺼내고
                for z in range(4):
                    nx = x+dx[z] # 4방향 검사
                    ny = y+dy[z]
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1: # 집 발견하는 경우
                        arr[nx][ny] = 0
                        cnt+=1 # 집의 개수를 증가
                        q.append((nx,ny)) # 큐에 노드 추가
            cnt_arr.append(cnt)
            
cnt_arr.sort() # 집 개수 정렬
print('총 단지수 :', len(cnt_arr)) # 단지수는 리스트의 길이
for i in cnt_arr:
    print('각 집의 개수 :',i)