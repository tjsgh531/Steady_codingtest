def solution(arr1, arr2):
    sortedarr1 = sorted(arr1)
    arrlength = len(arr1)

    for item in arr2:
        left = 0
        right = arrlength
        findnum = 0

        while left < right:
            mid = (left + right) // 2
            if  sortedarr1[mid] < item:
                left = mid+1
            elif sortedarr1[mid] > item:
                right = mid
            else:
                findnum = 1
                break
        print(findnum)

inputcount = int(input())
arr1 = list(map(int, input().split(' ')))
inputcount = int(input())
arr2 = list(map(int, input().split(' ')))
solution(arr1, arr2)