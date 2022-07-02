from collections import deque

def DFS(tomatos):
    maxcnt = 0
    dx = [0 ,0 , 1, -1]
    dy = [1, -1, 0, 0]

    #check도 넣어야 겠네 ...
    check =  [[False for _ in range(M)] for _ in range(N)]

    q = deque()
    for t in tomatos:
        q.append(t)

    while q:
        y, x, cnt = q.popleft()
        check[y][x] = True

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            # 토마토 없는 경우
            if graph[ny][nx] == -1:
                continue
            # 토마토 인경우
            elif graph[ny][nx] == 0 and check[ny][nx] == False:
                q.append((ny, nx, cnt+1))
                graph[ny][nx] = 1
                maxcnt = max(maxcnt, cnt+1)
            #다른 토마토와 만난경우
            else : 
                continue


    for i in range(N):
        for j in range(M):
            # 못 간 곳이 있으면 -1리턴
            if check[i][j] == False and graph[i][j] != -1:
                return -1
            else:
                return maxcnt

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
"""
M = 2
N = 2
graph = [
      [1,-1],
      [-1,1]]
"""
#모든 토마토 담기
tomato = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato.append((i, j, 0))

print(DFS(tomato))
