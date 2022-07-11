from collections import deque

def findshape(row, col):
    colsize = 0
    row_box_size = 0
    row_block_size = 0

    colcheck = False
    rowcheck = False

    cur_pos = (row, col)
    #row size check
    while not rowcheck and board[cur_pos[0], cur_pos[1]] == 0:
        row_box_size += 1
        checked[cur_pos[0]][cur_pos[1]] = True
        cur_pos = (cur_pos[0], cur_pos[1] + 1)
        if board[cur_pos[0]][cur_pos[1]] == 1:
            rowcheck = True
        else:
            row_block_size += 1

N = int(input())
u, v, w, x, y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
checked = [[False for _ in range(N)] for _ in range(N)]

temp_ans = (0, 0)
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and checked[i][j] == False:
            findshape(i, j)

