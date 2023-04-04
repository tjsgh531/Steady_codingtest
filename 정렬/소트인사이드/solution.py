import sys
input = sys.stdin.readline

N = input()
a = [0]* 10

for i in N:
    if(i == '\n'):
        break
    temp = int(i)
    a[temp]+=1

ans = ''
for idx, value in enumerate(a):
    for i in range(value):
        ans = f"{idx}"+ ans
print(ans)