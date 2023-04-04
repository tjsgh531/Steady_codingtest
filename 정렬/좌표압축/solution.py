import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
b = sorted(list(set(a)))

for i in a:
    print(b.index(i), end=" ")

# 시간초과