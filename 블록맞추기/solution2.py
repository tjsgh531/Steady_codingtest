from collections import deque

def dfs(row, col):
    global maxrow, maxcol
    visited[row][col] = True
    for i in range(4):
        nx = col + dx[i]
        ny = row + dy[i]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if not visited[ny][nx] and graph[ny][nx] == 1:
            maxrow = max(maxrow, ny)
            maxcol = max(maxcol, nx)
            dfs(ny, nx)

def bfs(row, col):
    q = deque()

    q.append((row, col))
    maxcol = col
    maxrow = row

    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visited[ny][nx] and graph[ny][nx] == 0:
                maxcol = max(maxcol, nx)
                maxrow = max(maxrow, ny)
                q.append((ny, nx))
    return maxrow, maxcol

def checkSize(min_row, min_col, max_row, max_col):    
    for i in range(min_row, max_row+1):
        for j in range(min_col, max_col+1):
            if not visited[i][j] and graph[i][j] == 0:
                bin_min_row, bin_min_col = i, j
                bin_max_row, bin_max_col = bfs(i, j)
                break
    if max_row == bin_max_row: #A타입
        if max_col - min_col != u -1:
            return False
        if bin_max_col - bin_min_col != y-1:
            return False
        if bin_min_col - min_col != w:
            return False
        if bin_max_row-bin_min_row != x -1:
            return False
    elif max_col == bin_max_col:#B타입
        if max_row - min_row != u-1:
            return False
        if max_row - bin_max_row != w:
            return False
        if bin_max_row - bin_min_row != y -1:
            return False
        if bin_max_col - bin_min_col != x-1:
            return False
    elif min_row == bin_min_row: #C타입
        if max_col-min_col != u-1:
            return False
        if max_col - bin_max_col != w:
            return False
        if bin_max_row - bin_min_row != x -1:
            return False
        if bin_max_col - bin_min_col != y-1:
            return False
    elif bin_min_col == min_col:#D타입
        if max_row- min_row != u-1:
            return False
        if bin_max_row-bin_min_row != y-1:
            return False
        if bin_max_col - bin_min_col != x-1:
            return False
        if bin_min_row-min_row != w:
            return False
    else:
        return False
    return min_row,min_col

    

        



N = int(input())
u, v, w, y, x = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
    
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            minrow, maxrow = i, i
            mincol, maxcol = j, j
            dfs(i, j)
            answer_row, answer_col = checkSize(minrow, mincol, maxrow, maxcol)
            print(answer_row +1, answer_col+1)