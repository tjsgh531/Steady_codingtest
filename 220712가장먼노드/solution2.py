#리겜리겜
from collections import deque

def solution(n, edge):
    adj = [[] for _ in range(n+1)]
    for i in edge:
        x = i[0]
        y = i[1]
        adj[x].append(y)
        adj[y].append(x)
    print(bfs(n, adj))

def bfs(n ,adj):
    visited = [-1 * (n+1)]
    q = deque()
    count = 0
    for item in adj[1]:
        q.append((item, count))
    visited[1] = count

    while q:
        next_node, cnt = q.popleft()
        #방문한 적 없음
        if visited[next_node] != -1:
            visited[next_node] = cnt+1
            for nt in adj[next_node]:
                q.append((nt, cnt+1))
    return max(visited)