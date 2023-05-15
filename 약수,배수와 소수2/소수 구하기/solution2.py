import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = set()

for i in range(N, M+1):
    for j in range(2, int(math.sqrt(i)) +1):
        if i % j == 0 :
            break
    else:
        print(i)
# 88% 에서 틀렸다라 ...