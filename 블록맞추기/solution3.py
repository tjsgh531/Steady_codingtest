from collections import deque

def checkSize(min_row, min_col, max_row, max_col):
    for i in range(min_row, max_row+1):
        for j in range(min_col, max_col+1):
            if visited[i][j] == False and graph[i][j]== 0:
                zero_min_row = i
                zero_min_col = j
                zero_max_row, zero_max_col = bfs(i, j, max_row, max_col)
                break
    # Type구분 + size check 하는 부분
    if max_row == zero_max_row: #A타입
        if max_col - min_row != u-1:
            return False
        if zero_min_col - min_col != w:
            return False
        if zero_max_row - zero_min_row != x-1:
            return False
        if zero_max_col - zero_min_col != y -1:
            return False
        if max_row + v >= N: #판 바깥을 나가면 안된다
            return False
        #다른 블록과 겹치면 안된다
        for k in range(max_row+1, max_row+1+v):
            for l in range(min_col, max_col):
                if graph[k][l] == 1:
                    return False
                visited[k][l] = True

    elif max_col == zero_max_col: #B타입
        if max_row - min_row != u-1:
            return False
        if max_row - zero_max_row != w:
            return False
        if zero_max_col - zero_min_col != x-1:
            return False
        if zero_max_row - zero_min_row != y-1:
            return False
        if max_col + v >= N: #판을 넘어 가면 안된다
            return False
        #다른 블록과 겹치면
        for k in range(min_row, max_row+1):
            for l in range(max_col+1, max_col+1+v):
                if graph[k][l] == 1:
                    return False
                visited[k][l] = True

    elif min_row == zero_min_row: #C타입
        if max_col - min_col != u-1:
            return False
        if max_col - zero_max_col != w:
            return False
        if zero_max_row - zero_min_row != x-1:
            return False
        if zero_max_col - zero_min_col != y -1:
            return False
        if min_row - v < 0:
            return False
        for k in range(min_row-v, min_row):
            for l in range(min_col, max_col+1):
                if graph[k][l] == 1:
                    return False
                visited[k][l] = True

    elif min_col == zero_min_col: #D타입
        if max_row - min_row != u -1:
            return False
        if zero_min_row - min_row != w:
            return False
        if zero_max_col - zero_min_col != x-1:
            return False
        if zero_max_row - zero_min_row != y-1:
            return False
        if min_col - v < 0 :
            return False
        for k in range(min_row, max_row+1):
            for l in range(min_col-v, min_col):
                if graph[k][l] == 1:
                    return False
                visited[k][l] = True
    else :
        return False
    return True

def bfs(row, col, maxrow, maxcol):
    q = deque()
    q.append((row, col))

    zeromaxrow = row
    zeromaxcol = col

    while q:
        y, x = q.popleft()
        visited[y][x] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < col or nx > maxcol or ny < row or ny > maxrow:
                continue
            if visited[ny][nx] == False and graph[ny][nx] == 0:
                zeromaxcol = max(zeromaxcol, nx)
                zeromaxrow = max(zeromaxrow, ny)
                q.append((ny, nx))
    return zeromaxrow, zeromaxcol
    
def dfs(row, col):
    global max_row, max_col
    x = col
    y = row
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[ny][nx] == False and graph[ny][nx] == 1:
            max_row = max(max_row, ny)
            max_col = max(max_col, nx)
            dfs(ny, nx)

N = int(input())
u, v, w, x, y = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and graph[i][j] == 1:
            min_row = i
            min_col = j
            max_row = i
            max_col = j
            dfs(i, j)
            temp = checkSize(min_row, min_col, max_row, max_col)
            if temp:
                answer.append((i, j))
print(len(answer))
for item in answer:
    y, x = item
    y += 1
    x += 1
    print(f"{y} {x}")