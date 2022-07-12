from collections import deque
#인접 노드 리스트를 모를때의 코드
#정말 드럽다

def solution(n, edge):
    visited = [0 for _ in range(n+1)]

    q = deque()
    for item in edge:
        if 1 in item:
            edge.remove(item)
            for i in item:
                if i != 1:
                    q.append((i, 1))

    while q:
        cur_node , count = q.popleft()
        if not visited[cur_node] :
            visited[cur_node] = count
            for item in edge:
                if cur_node in item:
                    edge.remove(item)
                    for i in item:
                        if i != cur_node:
                            q.append((i, count+1))
    return max(visited)

n = 6
edge = [[3,6], [4,3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))