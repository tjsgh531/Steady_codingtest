from collections import deque

def makeGraph(num):
    dup_graph = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] <= num: #못가는 땅
                dup_graph[i][j] = 1
    return dup_graph

def bfs(row, col):
    global dup_graph
    q = deque()

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q.append([row, col])

    while q:
        y, x = q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny <0 or ny >= N:
                continue
            if dup_graph[ny][nx] == 0:
                dup_graph[ny][nx] = 1
                q.append((ny, nx)) 

N = int(input())
graph = []
maxheight = 0
max_safe_zone = 0

for i in range(N):
    temp = list(map(int, input().split()))
    maxheight = max(maxheight, max(temp))
    graph.append(temp)

for n in range(1, maxheight+1):
    dup_graph = makeGraph(n)
    safe_zone = 0
    for i in range(N):
        for j in range(N):
            if dup_graph[i][j] == 0:
                bfs(i,j)
                safe_zone += 1
    max_safe_zone = max(max_safe_zone, safe_zone)

print(max_safe_zone)
