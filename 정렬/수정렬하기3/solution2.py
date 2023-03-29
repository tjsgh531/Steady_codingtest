import sys
input = sys.stdin.readline

N = int(input())

a = []

for _ in range(N):
    a.append(int(input()))

for i in sorted(a):
    print(i)

#메모리 초과