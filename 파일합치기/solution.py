def solution(data):
    cnt = 0
    while len(data) > 1:
        item1 = data.pop()
        item2 = data.pop()
        newitem = item1 + item2
        cnt += newitem
    
        data.append(newitem)
        data = sorted(data, reverse=True)
        print(f"data : {data}\t cnt : {cnt}")
    return cnt

answer = []
T = int(input())
for i in range(T):
    N = int(input())
    filesize = list(map(int, input().split()))
    print(sum(filesize))
    answer.append(solution(sorted(filesize, reverse=True )))

for i in answer:
    print(i)
