from collections import deque

#
def typeSort(row, col):
    iszero = False
    isactive = False
    cur_pos = (row, col)

    box_size = 0
    zero_size = 0

    #c타입 구분 못하겠는데 ...
    while not (isactive and board[cur_pos[0]][cur_pos[1]] == 0):
        box_size += 1

    #zero_size = 0이면 A B D형태, zero_size가 값이 있으면 C => C형 구분 가능
    #board[row+1][col] == 1 이면 A B 형태, 아니면 D => D형태 구분 가능
    #board[row+1][col + box_size -1] == 0이면 A 형태, 아니면 B => A, B 구분가능
    if zero_size != 0:

        return 'C', box_size
    if board[row+1][col] != 1:
        return 'D', box_size
    if board[row+1][col + box_size -1] == 0:
        return 'A', box_size
    else:
        return 'B', box_size

def checkShape(type, boxsize, row, col):
    box_height = 0
    if type == 'A':
        # x_size check
        cur_pos = (row+1, col)
        x_size = 0
        while board[cur_pos[0]][cur_pos[1]] == 1:
            x_size += 1
            box_height += 1
            cur_pos = (cur_pos[0] + 1, cur_pos[1])
        if x_size != x:
            return False
        # w & y size check
        cur_pos = (row, col)
        w_size = 0
        y_size = 0
        isactive = False
        while not (isactive and board[cur_pos[0]][cur_pos[1]] == 0):
            if 


    

N = int(input())
u, v, w, x, y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

temp_ans = (0, 0)
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 :
            box_type, box_width = typeSort(i, j)
            # u값이 안맞는 경우
            if box_type != 'D' and box_width != u:
                continue
    


