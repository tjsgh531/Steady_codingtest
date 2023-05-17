import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
while cnt ** 2 <= N:
    cnt += 1

print(cnt-1)