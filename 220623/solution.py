def solution(arr):
    sortedarr = sorted(arr)
    minend = 0
    count = 0
    for item in sortedarr:
        start = item[0]
        end = item[1]
        if start < minend: #겹침
            minend = min(minend, end)
        else: #안겹침
            count += 1
            minend = end
    print(count)

arrlen = int(input())
arr = []
for _ in range(arrlen):
    start, end = map(int, input().split())
    item = (start, end)
    arr.append(item)

#testarr = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
solution(arr)