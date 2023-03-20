N, X = map(int, input().split())

temp = list(map(int, input().split()))
for i in temp:
    if i < X:
        print(i, end=' ')
