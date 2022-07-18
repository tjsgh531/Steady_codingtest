def solution(data, cnt):
    cnt += sum(data)
    if len(data) > 1:
        target = sum(data) / 2
        temp = 0
        for i in range(len(data)):
            temp += data[i]
            if temp - target < target - temp - data[i]: # 현재가 중간값에 가깝다
                return solution(data[:i+1], cnt) + solution(data[i+1:], cnt)
            else:
                return solution(data[:i], cnt) + solution(data[i:], cnt)
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