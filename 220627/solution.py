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
    
