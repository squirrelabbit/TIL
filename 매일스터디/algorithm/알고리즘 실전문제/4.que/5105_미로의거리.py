def BFS():
    global answer
    while queue: 
        x,y = queue.pop(0)
        for i in range(4):#x,y 이동방법 4가지
            nx = x+dx[i] 
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:# 범위내에있고, 방문하지않을경우에 
                if not maze[nx][ny] == 1: #0이나 3이면 
                    visited[nx][ny] = True #방문한걸로 바꿈
                    queue.append((nx,ny)) # 새로운 좌표를 que에 추가
                    Distance[nx][ny] = Distance[x][y] +1 # 거리:카운트개념 +1 but for문이도는동안은 거리가같음
                    if maze[nx][ny] == 3: #도착지에 도달하면
                        answer = Distance[nx][ny] - 1 #답산출 but 위에서 1번 더 더해줘서 빼줌
                        break #최단거리
                        

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    
    dx = [0,0,-1,1]#이동경로
    dy = [1,-1,0,0]
    visited = [[False for _ in range(N)] for _ in range(N)]
    Distance = [[0]*N for _ in range(N)]  ###
    queue = []
    answer = 0 # 경로가 없으면 0으로 나와야하기 때문

    for i in range(N):  ###시작점찾기
        for j in range(N):
            if maze[i][j] == 2:
                queue.append((i,j))
                break
            
    
    BFS()

    print('#{} {}'.format(tc, answer))