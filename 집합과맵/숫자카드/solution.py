import sys
input = sys.stdin.readline

N = int(input())
dic = {value : 1 for value in list(map(int, input().split()))}
M = int(input())
for i in list(map(int, input().split())):
    if i in dic:
        print(1, end=" ")
    else:
        print(0, end=" ")