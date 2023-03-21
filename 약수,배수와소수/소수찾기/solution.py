N = int(input())
a = list(map(int, input().split()))
ans = 0
for num in a:
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt+=1
    if cnt == 2:
        ans +=1
print(ans)
