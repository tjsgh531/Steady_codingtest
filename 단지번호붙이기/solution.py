from collections import deque

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

"""
N = 7
graph = [
        [0,1,1,0,1,0,0],
        [0,1,1,0,1,0,1],
        [1,1,1,0,1,0,1],
        [0,0,0,0,1,1,1],
        [0,1,0,0,0,0,0],
        [0,1,1,1,1,1,0],
        [0,1,1,1,0,0,0]]
"""
total_count = 0 #섬의 개수

dx = [-1, 0, 0, 1]
dy = [0 , -1, 1, 0]

answer = []

#땅 면적 반환
def land(y, x):
    ans = 0
    q = deque()
    q.append([y,x])

    while q :
        y, x = q.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[ny][nx] == 1 :
                graph[ny][nx] = 0
                ans += 1
                q.append([ny, nx])
                
    return ans

#땅 구분 + 땅 개수 카운트
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            total_count += 1
            answer.append(land(i, j))


print(total_count)
for num in answer:
    print(num)