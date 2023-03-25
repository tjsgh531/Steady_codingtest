a = sorted(list(map(int, input().split())))

if(a[0]+a[1] <= a[2]):
    print((a[0]+a[1])*2-1)
else:
    print(sum(a))
