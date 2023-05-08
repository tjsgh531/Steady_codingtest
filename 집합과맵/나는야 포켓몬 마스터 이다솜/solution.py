import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_dict = dict()
name_dict = dict()

for i in range(1, N+1):
    name = input().strip()
    num_dict["{}".format(i)] = name
    name_dict[name] = i

for i in range(M):
    temp = input().strip()
    if temp in num_dict:
        print(num_dict[temp])
    else:
        print(name_dict[temp])