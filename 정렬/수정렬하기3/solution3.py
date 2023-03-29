import sys
input = sys.stdin.readline

N = int(input())

a = [0] * 10000

for _ in range(N):
    temp = int(input())
    a[temp-1]+=1

for idx,value in enumerate(a):
    if value == 0:
        continue
    else:
        for _ in range(value):
            print(idx+1)
