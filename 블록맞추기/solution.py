from collections import deque

#box_size부터 구해야겠다
def boxSize(row, col):
    q = deque()
    maxrow = row
    maxcol = col

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q.append((row, col))
    while q:
        y, x = q.popleft()
        visited[y][x] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny <0 or ny >= N:
                continue
            if board[ny][nx] == 1:
                maxrow = max(ny, maxrow)
                maxcol = max(nx, maxcol)
                q.append((ny, nx))
    return maxrow, maxcol

def checkSize(row, col, maxrow, maxcol):
    box_width = maxcol - col + 1
    box_height = maxrow - row + 1#

    #타입 구분 부터
    cur_pos = (row, col)
    c_sort = 0
    while board[cur_pos[0]][cur_pos[1]] == 1:
        c_sort += 1
        cur_pos = (cur_pos[0], cur_pos[1] + 1)
    if c_sort == maxrow - row +1:

    else: #C type
        if box_width != u:
            return False
        else:
            if c_sort != u - (w+y):
                return False
            else:

N = int(input())
u, v, w, x, y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

temp_ans = (0, 0)
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 :
            
    


