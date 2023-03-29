N = int(input())

for i in range(1, N):
    ans = i
    temp = i
    while temp > 0:
        ans += (temp % 10)
        temp = int(temp/10)
    if ans == N:
        print(i)
        break
else:
    print(0)
