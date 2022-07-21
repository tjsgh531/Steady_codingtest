def solution(n, cnt):
    print(f"n : {n}\t dp : {dp}")
    if n ==1:
        return
    cnt += 1

    if n % 3 == 0:
        dp[n//3] = min(dp[n//3], cnt) 
        solution(n//3, cnt)
    if n % 2 == 0:
        dp[n//2] = min(dp[n//2], cnt) 
    dp[n-1] = min(dp[n-1], cnt)
    solution(n-1, cnt)

N = int(input())
dp = [N for _ in range(N+1)]
solution(N, 0)
print(dp[1])
