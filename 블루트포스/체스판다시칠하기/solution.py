N, M = map(int, input().split())

a = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
b = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]

board = [ input() for _ in range(N)]

answer = N*M
for rowStart in range(N-7):
    for colStart in range(M-7):
        acnt = 0
        bcnt = 0
        rcnt = 0
        for row in range(rowStart, rowStart+8):
            ccnt = 0
            for col in range(colStart, colStart+8):
                if a[rcnt][ccnt] != board[row][col]:
                    acnt += 1
                if b[rcnt][ccnt] != board[row][col]:
                    bcnt +=1
                ccnt += 1
            rcnt += 1
        answer = min([answer, acnt, bcnt])

print(answer)