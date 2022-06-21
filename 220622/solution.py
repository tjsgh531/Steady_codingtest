def solution(arr, arrlen, target):
    maxidx = arrlen - 1
    curval = target
    count = 0

    while 1 :
        #이분 탐색으로 target의 위치 찾기
        minidx = 0
        while minidx < maxidx:
            mididx = (minidx+maxidx)//2
            if arr[mididx] < curval:
                minidx = mididx + 1
            elif arr[mididx] > curval:
                maxidx = mididx

        # unit 단위로 나누어 나머지가 있으면 한번 더 이분탐색, 없으면 끝
        unit = arr[minidx -1]
        count += curval//unit
        if curval % unit == 0:
            return count
        else:
            curval %= unit 

def inputfunc():
    arr = []
    arrlen, target = map(int, input().split())
    for _ in range(arrlen):
        temp = int(input())
        arr.append(temp)
    return target, arr, arrlen

target, arr, arrlen = inputfunc()
solution(arr, arrlen, target)
print(solution(arr, arrlen, target))