import sys
input = sys.stdin.readline

def dfs(cnt, left, right):
    new = abs(left - right)

    if new not in possible:
        possible.append(new)

    if cnt == N:
        return 0

    if dp[cnt][new] == 0:
        dfs(cnt + 1, left + weights[cnt], right)
        dfs(cnt+1, left, right + weights[cnt])
        dfs(cnt+1, left, right)
        dp[cnt][new] = 1

N = int(input())
weights = list(map(int, input().split()))
T = int(input())
marbles = list(map(int, input().split()))

dp = [[0] * 15001 for _ in range(N+1)]
possible = []

dfs(0, 0, 0)
for i in range(T):
    if marbles[i] in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')
