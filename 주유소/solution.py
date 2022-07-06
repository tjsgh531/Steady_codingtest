N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

minprice = price[0]
for i in range(N-1):
    if minprice < price[i]:
        price[i] = minprice
    else:
        minprice = price[i]

price.pop()

ans = 0
for dis, pr in zip(dist, price):
    ans += dis * pr
print(ans)