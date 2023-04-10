import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(set(arr))

dic = {value : idx for idx, value in enumerate(arr2)}

for i in arr:
    print(dic[i], end=" ")