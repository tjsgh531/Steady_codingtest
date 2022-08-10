def solution():
    maxvalue = 0
    for i in range(2):
        for j in range(3):
            maxvalue = max(maxvalue, dp[i][j])

    for i in range(3, N):
        if items[i-1] == 0:
            dp[0][i] = maxvalue+ items[i]
        else:
            dp[0][i] = max(dp[0][i-2], dp[1][i-2])+ items[i]
        dp[1][i] = dp[0][i-1]+items[i]
        maxvalue = max(maxvalue, dp[0][i], dp[1][i])
    return maxvalue

N = int(input())
items = [int(input()) for _ in range(N)]

if N >= 3:
    dp = [ 
        [items[0], items[1], items[0]+items[2]] + [0] * (N-3),
        [0, items[0]+items[1], items[1]+items[2]] + [0] * (N-3)
    ]    
    #dp[0][i] => i번째 전 잔(i-1)을 먹지 않은 상태에서, i번째 잔을 먹을 때 최대값 = max(dp[0][i-2], dp[1][i-2])+ items[i]
    #dp[1][i] => i번째 전 잔(i-1)을 먹은 상태에서, i번째 잔을 먹을 때 최대값 = dp[0][i-1] + items[i]
    print(solution())
else:
    print(sum(items))