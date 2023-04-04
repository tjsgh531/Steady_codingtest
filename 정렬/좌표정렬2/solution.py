import sys
input = sys.stdin.readline

a = [[] for _ in range(200001)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    a[y+100000].append(x)

for idx, xlist in enumerate(a):
    if xlist:
        for x in sorted(xlist):
            print(f"{x} {idx-100000}")

