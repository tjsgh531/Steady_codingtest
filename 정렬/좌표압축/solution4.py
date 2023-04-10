import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

answer = {}

temp = []
for idx, value in enumerate(sorted(list(set(a)))):
    temp.append((value, idx))

for item in temp:
    if item[0] in answer:
        continue
    
    answer[item[0]] = item[1]

for val in a:
    print(answer[val], end=" ")
