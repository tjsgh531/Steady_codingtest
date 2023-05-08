import sys
input = sys.stdin.readline

num_dict = dict()
N = int(input())

temp = list(map(int, input().split()))
for i in temp:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

M = int(input())
temp = list(map(int, input().split()))
for i in temp:
    if i in num_dict:
        print(num_dict[i], end=" ")
    else:
        print(0, end=" ")