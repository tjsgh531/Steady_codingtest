N, M = map(int, input().split())

graph = [list(input().split()) for _ in range(N)]

def DFS(x, y);
    check = [[True for _ in range(M)]]
    row = [True]
    for i in range(1, N-1):
        row = [True]
        for j in range(1, M-1):
            row.append(False)
        row.append(True)
        check.append(row)

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]