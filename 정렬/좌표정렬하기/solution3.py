import sys
input = sys.stdin.readline

a = [[] for _ in range(200001)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    a[x+100000].append(y)

for idx, ylist in enumerate(a):
    if ylist:
        for y in sorted(ylist):
            print(f"{idx-100000} {y}")

