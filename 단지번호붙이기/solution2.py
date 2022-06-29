from collections import deque

def findland(row, col):
    count = 1
    graph[row][col] = 0

    q = deque()
    q.append([row, col])
    
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= N or ny < 0 or nx >= N or nx < 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append([ny, nx])
                count += 1
    return count


total_count = 0
answer = []

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

N = int(input())
graph = [ list(map(int, input())) for _ in range(N) ]
"""
N = 7
graph = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0]
]
"""

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            total_count += 1
            answer.append(findland(i, j))

print(total_count)
for i in sorted(answer):
    print(i)