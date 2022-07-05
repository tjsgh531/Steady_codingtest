N = int(input())
P = list(map(int, input().split()))

ans = 0
for i in sorted(P):
    ans += i * N
    N -= 1
    
print(ans)