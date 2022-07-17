
def solution(data, cnt):
    if len(data) > 1:
        minval = data[0]+data[1]
        minidx = 0
        for i in range(1, len(data)-1):
            if data[i]+data[i+1] < minval:
                minidx = i
                minval = data[i] + data[i+1]
        data[minidx:minidx+2] = [minval]
        cnt += minval
        print(f"data : {data} \t cnt : {cnt}")
        return solution(data, cnt)
    else:
        return cnt

answer = []
T = int(input())
for i in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    answer.append(solution(data, 0))

for i in answer:
    print(i)

