# 유클리드 호제법을 이용하여 풀어보자.

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
ans = A*B
while B != 0:
    a = min(A, B)
    b = max(A, B)
    A = a
    B = b
    
    B = B % A
print(ans//A)