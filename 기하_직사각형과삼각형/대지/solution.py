N = int(input())

if N < 2:
    print(0)
else:
    posX = []
    posY = []
    for _ in range(N):
        a, b = map(int, input().split())
        posX.append(a)
        posY.append(b)
    
    minX = min(posX)
    maxX = max(posX)
    minY = min(posY)
    maxY = max(posY)

    print((maxX-minX)*(maxY-minY))