import sys
input = sys.stdin.readline

dic = []
N, M = map(int, input().split())

for _ in range(N):
    temp = input()
    dic.append(temp)

dic = list(set(dic))
ans = 0
for _ in range(M):
    temp = input()
    if temp in dic:
        ans += 1
print(ans)