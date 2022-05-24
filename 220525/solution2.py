def solution(arr, pickcount):
    sortedarr = sorted(arr)
    sortedarrlength = len(sortedarr)
    maxnum = sortedarr[-1]
    minnum = sortedarr[0]

    idelNum = []
    stride = (maxnum - minnum)// 2
    temp = minnum
    
    for _ in range(pickcount-2):
        temp += stride
        idelNum.append(temp)
    idelNum.append(maxnum)
    
    mingap = maxnum - minnum
    pickednum = [minnum]
    for item in idelNum:
        left = 0
        right = sortedarrlength
        while left < right:
            mid = (left + right)//2
            if sortedarr[mid] <= item:
                left = mid + 1
            elif sortedarr[mid] > item:
                right = mid
        idelnum = sortedarr[mid-1] if item - sortedarr[mid-1] < sortedarr[mid] - item else sortedarr[mid]
        
        gap = idelnum - pickednum[-1]
        mingap = gap if gap < mingap else mingap
        pickednum.append(idelnum)
    print(mingap)
            
inputcount = int(input())
picknum = int(input())
arr = []
for _ in range(inputcount):
    temp = int(input())
    arr.append(temp)

solution(arr,picknum)