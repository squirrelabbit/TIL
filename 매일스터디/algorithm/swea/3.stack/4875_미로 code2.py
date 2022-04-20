T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list((list(map(int,list(input()))))) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    dx = [0,0,-1,1]#이동경로
    dy = [1,-1,0,0]
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x1,y1 = i,j
                break
    # 스택이 비었다는 건 갈 수 있는 길이 없어 되돌아오면서 길을 탐색해도 길이 없음
    stack = []
    answer = 0 # 경우가없으면 0반환
    while stack:
        # 현재 위치
        x,y = x1,y1
        # 위치 값이 3이면 도착
        if maze[x][y] == 3:
            answer = 1   #=>반환
            break

        # 길을 따라 이동해보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 있는 길인지 확인
            # 갈 수 없는 길 : 미로를 벗어나는 경우, 벽, 이미 방문한 곳
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                # 갈 수 있는 길이니 이동해보기
                stack.append((nx,ny))
                visited[nx][ny] = 1
                break
        # break을 만나지 않았다는 것은 갈 길이 없다는 것 -> 한 칸 되돌아 가보자
        else:
            stack.pop()

    print('#{} {}'.format(tc, answer))
    