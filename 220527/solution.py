def solution(arr, n):
    sortedarr = sorted(arr)
    mindis = 1
    maxdis = sortedarr[-1] -sortedarr[0]

    result = 0

    while mindis < maxdis :
        middis = (maxdis + mindis) // 2

        if check(n-1, sortedarr, middis):
            result = middis
            mindis = middis+1
        else:
            maxdis = middis

    return result

def check(n, sortedarr, dis):
    cnt = 0
    preval = sortedarr[0]

    for item in sortedarr:
        if cnt == n:
            return True
            
        if item - preval >= dis:
            cnt += 1
            preval = item
    else:
        return False

arrlen, choicenum = map(int, input().split(' '))
arr = []
for _ in range(arrlen):
    item = int(input())
    arr.append(item)
print(solution(arr, choicenum))
#solution([1,2,8,4,9], 3)