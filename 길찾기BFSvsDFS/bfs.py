# queue로 구현

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, row, col):
    queue = deque()
    queue.append((row, col))
    graph[row][col] = 0
    count = 1

    while queue:
        y, x  = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))
                count += 1
    return count

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
cnt = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)