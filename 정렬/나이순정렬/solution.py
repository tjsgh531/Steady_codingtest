import sys
input = sys.stdin.readline

a = [[] for _ in range(201)]
N = int(input())
for _ in range(N):
    data = input().split()
    age = int(data[0])
    name = data[1]
    a[age].append(name)

for age, namelist in enumerate(a) :
    if len(namelist) != 0:
        for name in namelist:
            print(f"{age} {name}")