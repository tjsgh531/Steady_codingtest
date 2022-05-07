from collections import deque

def solution(total, selectarr):
    totalnum = total

    result = 0;
    currentarr = deque(selectarr)

    for i in range(len(selectarr)):
        num = currentarr.popleft()    
        rot =  num -1
        reverserot = totalnum- num + 1

        if rot > reverserot: #reverserot 을 해야함
            for idx in range(len(currentarr)):
                item = currentarr.popleft()
                if item > num:
                    currentarr.append(item-num)
                else:
                    currentarr.append(totalnum-(num - item))
            result += reverserot
 
        else: # rot을 할 경우
            for idx in range(len(currentarr)):
                item = currentarr.popleft()
                if item > num:
                    currentarr.append(item-num)
                else:
                    currentarr.append(totalnum-(num-item))
            result += rot
        totalnum -=1
    return result

input_st = input().split(' ')
totalnum = int(input_st[0])

selectlist = []
input_nd = input().split(' ')
for i in input_nd:
    selectlist.append(int(i))

print(solution(totalnum, selectlist))