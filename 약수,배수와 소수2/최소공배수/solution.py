import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    
    for i in range(B, B*A+1):
        if i % A == 0 and i % B == 0:
            print(i)
            break
# 시간초과