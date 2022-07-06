from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
print(visited)


dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

def init():
    rx, ry, bx, by = [0] * 4
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y , dx, dy):
    count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])

            #파란 구슬이 O를 만나경우 무효처리
            if board[next_bx][next_by] == 'O':
                continue
            #빨간 구슬이 O를 만난경우 depth print하고 끝내기
            if board[next_rx][next_ry] == 'O':
                print(depth)
                return
            #같은 좌표인경우 => count가 필요한 이유
            if next_rx == next_bx and next_ry == next_by:
                if r_count > b_count:
                    next_rx -=dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
            
            #예외 경우가 아닌경우(끝나지도 오류나지도 않은 경우)        
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth+1))
    print(-1)

bfs()