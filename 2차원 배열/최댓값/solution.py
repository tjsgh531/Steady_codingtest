A = [list(map(int, input().split(' '))) for _ in range(9)]
maxValue = [-1, -1, -1]
for rowidx, row in enumerate(A):
    for colidx, item in enumerate(row):
        if maxValue[0] < item : 
            maxValue = [item, rowidx, colidx]
print(maxValue[0])
print(maxValue[1]+1, maxValue[2]+1)