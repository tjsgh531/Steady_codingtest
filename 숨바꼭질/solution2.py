from collections import deque

def solution():
    q = deque()
    global N
    
    count = 0
    while N*2 < K:
        count += 1
        N *= 2

    move = [-1, 1, 2]
    q.append((N, count))

    while q:
        item = q.popleft()
        if item[0] == K:
            print(item[1])
            return

        for i in move:
            if i == 2:
                new_item = (item[0]*2, item[1]+1)
            else:
                new_item = (item[0] +i, item[1]+1)
            q.append(new_item)


N, K = map(int,input().split())
solution()
