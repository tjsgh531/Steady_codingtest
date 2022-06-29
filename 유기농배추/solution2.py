from collections import deque

def makegraph(col, row, num):
    graph = [[0 for _ in range(col)] for _ in range(row)]
    
    #배추 심기
    for _ in range(num):
        x, y = map(int, input().split())
        graph[y][x] = 1

    
    return [row, col, graph]

def solution(y, x):
    q = deque()
    q.append([y, x])

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    while q:
        y, x = q.popleft()
        graph[y][x] = 0


        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append([ny, nx])



N = int(input()) #test개수

#입력 처리
graphs = []
for _ in range(N):
    M, N, K = map(int, input().split())
    graphs.append(makegraph(M, N, K))

#출력 처리
for item in graphs:
    count = 0
    M = item[0]
    N = item[1]
    graph = item[2]

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                count += 1
                solution(i,j)
    print(count)
