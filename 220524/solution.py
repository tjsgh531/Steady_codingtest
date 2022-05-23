import bisect
from collections import deque

def solution(arr):
    templist = []
    templist.append(arr[0])
    idxlist = []

    maxidx = 0
    for item in arr:
        targetidx = bisect.bisect_left(templist, item)
        idxlist.append(targetidx)

        if targetidx > maxidx:
            maxidx = targetidx
            templist.append(item)
        else:
            templist[targetidx] = item
    print(idxlist)

    maxidxlist = max(idxlist)
    modiidxlist = reversed(list(enumerate(idxlist))) 
    
    result = deque()
    for item in modiidxlist:
        if item[1] == maxidxlist:
            result.appendleft(arr[item[0]])
            maxidxlist -= 1
    print(result)        

solution([5, 8, 10, 12, 15, 3 , 100, 15])