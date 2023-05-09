import sys
input = sys.stdin.readline

str1 = input()

ans = set()
for i in range(1, len(str1)+1):
    for j in range(len(str1)-i):
        ans.add(str1[j:j+i])
print(len(ans))