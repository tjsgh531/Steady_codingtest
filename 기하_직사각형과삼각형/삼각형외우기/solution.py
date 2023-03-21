a = [int(input()) for _ in range(3)]

if sum(a) != 180:
    print("Error")
else:
    for i in a:
        if a.count(i) == 3:
            print("Equilateral")
            break
        elif a.count(i) == 2:
            print("Isosceles")
            break
    else:
        print("Scalene")
