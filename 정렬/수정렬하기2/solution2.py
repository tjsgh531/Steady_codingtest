N = int(input())

a = [0] * 1000000
for _ in range(N):
    temp = int(input())
    a[temp-1] = temp

cnt =0
for i in a:
    if i != 0:
        print(i)
        cnt +=1
        if cnt == N:
            break

# 시간초과