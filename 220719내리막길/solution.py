import sys
input = sys.stdin.readline

def dfs(row, col):
    global answer
    if row == N-1 and col == M-1:
        answer += 1
        return 0

    cur_val = graph[row][col]
    for i in range(4):
        nx = col + dx[i]
        ny = row + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if  graph[ny][nx] < cur_val:
            dfs(ny, nx)
    return 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dfs(0, 0)
print(answer)