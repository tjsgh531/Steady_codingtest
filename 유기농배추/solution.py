from collections import deque

def solution():
    ans = 0
    global maxrow, maxcol
    for i in range(maxrow):
        for j in range(maxcol):
            if graph[i][j] == 1:
                ans += 1
                linkland(i, j)
    print(ans)

def linkland(row, col):
    global maxrow, maxcol
    q = deque()
    q.append([row, col])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= maxrow or nx < 0 or nx >= maxcol:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append([ny,nx])
# N = int(input())
graphs = []


for _ in range(N):
    M,N,K = map(int, input().split())
    graph = [[0 * M] for _ in range(N)]
    for _ in range(K):
        row, col = map(int, input().split())
        graph[row][col] = 1
    graphs.append([M, N, graph])

"""
graphs = [ [10, 8, [
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            ]
        ]
"""

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

for item in graphs:
    maxcol = item[0]
    maxrow = item[1]
    graph = item[2]

solution()