import sys
input = sys.stdin.readline

N = int(input())

tower = [[0] * (N+1) for _ in range(N+1)]
tower[0][0] = 1

def blockValue(row, col):
    up = 0
    left = 0
    
    if tower[row][col] != 0:
        return tower[row][col]
    
    if row - 1 >= 0:
        up = blockValue(row-1, col)
    if col - 1 >= 0:
        left = blockValue(row, col-1)

    tower[row][col] = up + left
    return up + left


ans = 0
for i in range(N+1):
    ans += blockValue(i, N-i)

print(ans)