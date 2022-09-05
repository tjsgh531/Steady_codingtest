import sys
from collections import deque

input = sys.stdin.readline;

def check33(row, col):
    border_row = row // 3
    border_col = col // 3

    visited = [[False for _ in range(9)] * 9]

    q = deque()
    q.append((row, col))
    while q:
        item = q.popleft()

        for i in range(4):
            ny = dy[i] + item[0]
            nx = dx[i] + item[1]

            if visited:
                continue

            if ny < 0 or ny // 3 != border_row or nx < 0 or nx // 3 != border_col:
                continue

            if board[ny][nx] in check_board:
                check_board.remove(board[ny][nx])

            visited[ny][nx] = True
            q.append((ny, nx))

def checkrow(row):
    for i in range(9):
        item = board[row][i]
        if item in check_board :
            check_board.remove(item)

def checkcol(col):
    for i in range(9):
        item = board[i][col]
        if item in check_board:
            check_board.remove(item)

board = [list(map(int, input().split())) for _ in range(9)]
blanks = deque()
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blanks.append((i, j))

while blanks:
    blank = blanks.popleft()
    check_board = list(range(1,10))

    checkrow(blank[0])
    checkcol(blank[1])
    check33(blank[0], blank[1])

    if len(check_board) == 1:
        board[blank[0]][blank[1]] = check_board.pop()
    else:
        blanks.append(blank)


for i in range(9):
    for j in range(9):
        print(board[i][j], end=' ')
    print()