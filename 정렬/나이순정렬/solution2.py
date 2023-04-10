import sys
input = sys.stdin.readline

N = int(input())

answer = [[] for _ in range(201)]
for _ in range(N):
    temp = input().split()
    age = int(temp[0])
    name = temp[1]
    answer[age].append(name)

for idx, value in enumerate(answer):
    if value:
        for name in value:
            print(f"{idx} {name}")
