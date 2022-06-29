import sys #왜 필요하지??

sys.setrecursionlimit(10**6) #이거 이차배열 크기 제한 해주는 거였는데
from collections import deque

N = int(input()) # mapsize
graph = [list(map(int, input().split())) for _ in range(N)] # 1110000111 이런식으로 입력 받음
check = [[False] *  N for _ in range(N)]

dx = [-1 , 0 , 0 , 1]
dy = [0 , -1 , 1 , 0]

ans = sys.maxsize # 이건 뭘까요??
count = 1

# map print
def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j])
        print()

#섬 별로 숫자 붙여주기
def dfs(y, x):
    global count
    check[y][x] = True
    graph[y][x] = count

    for i in range(4):
        ny, nx = y + dy[i], x+ dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if check[ny][nx] == False and graph[ny][nx]:
            dfs(ny, nx)

#받아온 섬 숫자에 해당하는 섬을 찾는 함수
def bfs(num):
    global ans
    dist = [[-1] * N for _ in range(N)] #땅으로 부터 거리를 측정하기위한 graph 사본
    q = deque()

    for i in range(N):
        for j in range(N):
            if graph[i][j] == num:
                q.append([i, j])
                dist[i][j] = 0
        
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if graph[ny][nx] > 0 and graph[ny][nx] != num:
                ans = min(ans, dist[y][x])
                return

            if graph[ny][nx] == 0 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append([ny, nx])

for i in range(N):
    for j in range(N):
        if check[i][j] == False and graph[i][j] == 1:
            dfs(i, j)
            count += 1

for i in range(1, count):
    bfs(i)

print(ans)
