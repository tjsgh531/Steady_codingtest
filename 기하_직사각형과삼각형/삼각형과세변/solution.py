while(1):
    a = list(map(int,input().split()))
    if sum(a) == 0:
        break

    elif(0 >= sum(a)-2*max(a)):
        print("Invalid")

    elif a.count(a[0]) == 3:
        print("Equilateral")

    elif a.count(a[0]) == 2 or a.count(a[1]) == 2:
        print("Isosceles")

    else:
        print("Scalene")

