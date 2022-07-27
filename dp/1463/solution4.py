import sys
input = sys.stdin.readline

N = int(input())
dp = [0] + [i for i in range(N)]

print(dp) 
for idx, value in enumerate(dp):

    if idx * 3 <= N:
        dp[idx*3] = min(dp[idx*3], value+1)
    if idx * 2 <= N:
        dp[idx*2] = min(dp[idx*2], value + 1)
    if idx > 0:
        dp[idx] = min(dp[idx-1]+1, value)
print(dp)