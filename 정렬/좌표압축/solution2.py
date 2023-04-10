import sys
input = sys.stdin.readline
import math 

N = int(input())
a = [0] * int(math.pow(10, 9) *2 + 1) #메모리 에러

b = list(map(int, input().split()))

for i in b:
    a[i+math.pow(10,9)] = 1

cnt = 0
for i in a:
    if i != 0:
        print(f"{cnt}", end=' ')
        cnt += 1
