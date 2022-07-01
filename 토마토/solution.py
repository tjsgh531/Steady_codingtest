from collections import deque

def DFS(tomatos):
    maxcnt = 0
    dx = [0 ,0 , 1, -1]
    dy = [1, -1, 0, 0]
#check도 넣어야 겠네 ...
    q = deque()
    for t in tomatos:
        q.append(t)

    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            # 토마토 없는 경우
            if graph[ny][nx] == -1:
                continue
            # 토마토 인경우
            elif graph[ny][nx] == 0:
                q.append((ny, nx, cnt+1))
                maxcnt = max(maxcnt, cnt+1)
            #다른 토마토와 만난경우
            else : 
                continue

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

#모든 토마토 담기
tomato = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            tomato.append((i, j, 0))

DFS(tomato)
