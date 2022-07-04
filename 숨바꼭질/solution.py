#메모리 초과
from collections import deque

def bfs():
    q = deque()
    move = (-1, 1, 2)
    q.append((N, 0))

    while q:
        item = q.popleft()
        if item[0] == K:
            print(item[1])
            return

        for i in move:
            if i == 2:
                new_item = (item[0]*2, item[1]+1)
                q.append(new_item)
            else:
                new_item = (item[0] + i, item[1]+1)
                q.append(new_item)

N, K = map(int,input().split())
bfs()