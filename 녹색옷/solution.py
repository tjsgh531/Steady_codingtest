def dfs(row, col, sum):
    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        
        if ny == N-1 and nx == N-1:
            if dp[ny][nx] != 0:
                dp[ny][nx] = min(dp[ny][nx], sum + graph[ny][nx])
            else:
                dp[ny][nx] = sum + graph[ny][nx]
        else:
            if dp[ny][nx] > sum + graph[ny][nx]:
                continue
            else:
                dp[ny][nx] = sum + graph[ny][nx]
                dfs(ny, nx, dp[ny][nx])


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
while 1:
    N = int(input())
    
    if N == 0 :
        break
    else :
        count +=1
        dp = [[0] * N for _ in range(N)]

        graph = [list(map(int, input().split())) for _ in range(N) ]
        dp[0][0] = graph[0][0]
        dfs(0, 0, dp[0][0])
        print(f"Problem {count}: {dp[N-1][N-1]}")

