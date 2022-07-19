from collections import deque
import sys
input = sys.stdin.readline

def bfs(row, col):
    answer = 0
    q = deque()
    q.append((row, col))
    while q:
        y, x = q.popleft()
        cur_val = graph[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[ny][nx] < cur_val:
                if ny == N-1 and nx == M-1:
                    answer += 1
                else:
                    q.append((ny, nx))
    return answer

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
print(bfs(0, 0))