from collections import deque

def bfs(n):
    q = deque()
    q.append((n, 0))
    mincnt = n
    success = False

    while q:
        val, cnt = q.popleft()
        if val == 1:
            mincnt = min(mincnt, cnt)
            success = True
        else:
            if success and cnt >= mincnt :
                continue
            if val % 3 == 0:
                q.append((val/3, cnt+1))
            if val % 2 == 0:
                q.append((val/2, cnt+1))
            q.append((val-1, cnt+1))
    return mincnt

N = int(input())
print(bfs(N))
