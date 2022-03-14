def DFS(x,y):
    for i in range(4):#x,y 이동방법 4가지
        nx = x+dx[i] 
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:# 범위내에있고, 방문하지않을경우에 
            if not maze[nx][ny]: #0이면
                visited[nx][ny] = True #방문한걸로 바꿈
                if DFS(nx,ny):# 반복되어서 true가 나옴 =>3에 도착
                    return True
            elif maze[nx][ny] == 3:
                return True 
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list((list(map(int,list(input()))))) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    dx = [0,0,-1,1]#이동경로
    dy = [1,-1,0,0]
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:#시작지점
                answer = 1 if DFS(i,j) else 0 #DFS가 true 일때 1
    print('#{} {}'.format(tc, answer))
    