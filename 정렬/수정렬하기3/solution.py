import sys

input = sys.stdin.readline

N = int(input())
a = [0] * 10000

for _ in range(N):
    temp = int(input())
    a[temp-1] = temp

for i in a:
    if i == 0:
        continue
    else:
        print(i)