N, M = map(int, input().split())

graph = [list(input().split()) for _ in range(N)]

check = [[True for _ in range(M)]]
row = [True]
for i in range(1, N-1):
    row = [True]
    for j in range(1, M-1):
        row.append(False)
    row.append(True)
    check.append(row)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            curRx = j
            curRy = i
        elif graph[i][j] == 'B':
            curBx = j
            curBy = i
        elif graph[i][j] == 'O':
            exitx = j
            exity = i


def move(dir):
    global curRx, curRy, curBx, curBy
    move = False
    RfindE = False
    BfindE = False
    #UP
    if dir == 1:
        while check[curRy][curRx] == False or RfindE or BfindE:
            check[curRy][curRx] = True 
            # 빨간 구슬 움직일 수 없다
            if check[curRy -1][curRx] == True:
                break
            # 빨간 구슬 움직일 수 있을 경우
            else:
                # exit를 만난 경우
                if graph[curRy -1][curRx] == 'O':
                    RfindE = True


                move = True
                curRy -= 1


            # 파란 구슬 움직일 수 있을 때
            if graph[curBy-1][curBx]== '.':
                curBy = curBy-1
            #파란 구슬이 exit를 찾은 경우
            elif graph[curBy-1][curBx] == 'O':
                BfindE = True

