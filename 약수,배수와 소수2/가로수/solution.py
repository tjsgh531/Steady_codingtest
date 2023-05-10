import sys
import math
input = sys.stdin.readline

N = int(input())
gap=[]
pre_val = 0
for _ in range(N):
    n = int(input())
    
    if pre_val == 0:
        pre_val = n
        continue
    
    gap.append(n - pre_val)
    pre_val = n

gcd = math.gcd(*gap)

ans = 0
for item in gap:
    ans += (item // gcd) -1

print(ans)