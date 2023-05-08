import sys
input = sys.stdin.readline

name_dict = dict()
N, M = map(int, input().split())

for _ in range(N):
    name = input().strip()
    name_dict[name] = 1

ans = 0
ans_name = []
for _ in range(M):
    name = input().strip()
    if name in name_dict:
        ans += 1
        ans_name.append(name)

print(ans)
for name in sorted(ans_name):
    print(name)