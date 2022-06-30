from collections import deque

def DFS(row, col):


M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            