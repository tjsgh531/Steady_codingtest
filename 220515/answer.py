def solution(n, times):
    answer = 0
    start, end, mid = 1, times[-1] * n, 0 #times가 sort 되어있다고 생각하고 푼것

    while start < end:
        mid = (start + end) // 2
        total = 0
        for time in times:
            total += mid // time

        if total >= n:
            end = mid
        else:
            start = mid + 1
    answer = start
    return answer