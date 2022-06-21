def solution(arr, target):
    ans = 0
    for unit in reversed(arr):
        if target == 0 :
            break
        ans += target // unit
        target %= unit
    return ans
    
def inputfunc():
    arr = []
    arrlen, target = map(int, input().split())
    for _ in range(arrlen):
        temp = int(input())
        arr.append(temp)
    return target, arr

target, arr = inputfunc()
print(solution(arr, target))