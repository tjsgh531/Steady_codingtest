import itertools

N, M = map(int, input().split())
a = list(map(int, input().split()))

comb = itertools.combinations(a, 3)
answer = 0
for item in comb:
    temp = sum(item)
    if temp > M:
        continue
    else :
        if answer < temp:
            answer = temp
print(answer)