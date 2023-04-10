import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

answer = [0] * N

sortedA = []
for idx, value in enumerate(a):
    sortedA.append((value, idx))

sortedA = sorted(sortedA)

for idx, value in enumerate(sortedA):
    answer[value[1]] = idx

for ans in answer:
    print(ans, end=" ")