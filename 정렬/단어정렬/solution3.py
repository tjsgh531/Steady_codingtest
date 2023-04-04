import sys
input = sys.stdin.readline

N = int(input())
a = []
for _ in range(N):
    temp = input().strip()
    a.append(temp)

a = list(set(a))
a.sort()
a.sort(key = len)

for word in a:
    print(word)

