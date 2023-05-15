import sys
input = sys.stdin.readline

M, N = map(int, input().split())

num_list = set(range(M, N+1))

for i in range(2, N+1):
    if 2*i > N+1:
        break
    for j in range(2*i, N+1, i):
        if j in num_list:
            num_list.remove(j)

for i in num_list:
    print(i)

