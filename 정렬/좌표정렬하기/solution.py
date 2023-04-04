import sys
input = sys.stdin.readline

a = [[] for _ in range(100001)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    a[x].append(y)

for idx, ylist in enumerate(a):
    if ylist:
        for y in sorted(ylist):
            print(f"{idx} {y}")
#틀렸습니다 ㅜㅜ
