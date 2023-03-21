posX = []
posY = []

for _ in range(3):
    a, b = map(int, input().split())
    posX.append(a)
    posY.append(b)

ans =[0, 0]
for x in posX: 
    if posX.count(x) == 1:
        ans[0] = x
for y in posY:
    if posY.count(y) == 1:
        ans[1] = y
print(f"{ans[0]} {ans[1]}")