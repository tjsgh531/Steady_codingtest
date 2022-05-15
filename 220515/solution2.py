import heapq

def solution(n, times):
    content = []
    result = 0
    for item in times:
        heapq.heappush(content, [item,item])
    
    for i in range(n):
        minitem = heapq.heappop(content)
        if minitem[0] > result:
            result = minitem[0]
        newitem = [minitem[0] + minitem[1], minitem[1]]
        heapq.heappush(content, newitem)
    return result

print(solution(6, [7, 10]))