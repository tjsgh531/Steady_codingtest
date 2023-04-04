import sys
input = sys.stdin.readline

N = int(input())

a = [[] for _ in range(100001)]
for _ in range(N):
    x, y = map(int, input().split())
    a[x].append(y)


for idx, value in enumerate(a) :
    if len(value) != 0:
        for y in sorted(value):
            print(f"{idx} {y}")