import heapq

def solution(n, times):
    currenttime = []
    for time in times:
        item = [0, time]
        currenttime.append(item)
    
    for j in range(n):
        temp = []
        for i in range(len(currenttime)):
            costtime = currenttime[i][0] + currenttime[i][1]
            item = (costtime, i)
            heapq.heappush(temp, item)
        target = heapq.heappop(temp)
        currenttime[target[1]][0] = target[0]

    return max(currenttime)[0]
    result = []
    for i in range(len(currenttime)):
        item = -currenttime[i][0]
        heapq.heappush(result, item)

    return -result[0]

print(solution(6, [7, 10]))