import sys
input = sys.stdin.readline

n = int(input())
log = {}
for _ in range(n):
    temp = input().split()
    if temp[1] == "enter":
        log[temp[0]] = 1
    else:
        del log[temp[0]]

for key in sorted(log.keys(), reverse=True):
    print(key)