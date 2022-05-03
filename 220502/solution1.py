from collections import deque

def solution(cardnum, skills):
    deq = deque(range(1, cardnum+1))
    result = deque()

    for i in reversed(list(skills)):
        item = deq.popleft()
        if i == 1:
            result.appendleft(item)
        elif i == 3:
            result.append(item)
        else:
            temp = result.popleft()
            result.appendleft(item)
            result.appendleft(temp)
    return result

cardnum = int(input())
skills = map(int, input().split())
result = solution(cardnum, skills)
for i in result:
    print(i, end=' ')