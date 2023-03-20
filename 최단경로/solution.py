from operator import truediv
import sys
input = sys.stdin.readline

def getsmallest():
    min_value = 10
    min_idx = V+1
    for i in range(1, V+1):
        if visited[i] : continue
        if min_value > answer[i]:
            min_value = answer[i]
            min_idx = i
    return min_idx

def solution():
    cur = getsmallest()
    while  cur != V+1:
        visited[cur] = True
        for i in range(1, V+1):
            if graph[cur][i] != 'INT':
                if answer[i] == 'INT':
                    answer[i] = answer[cur] + graph[cur][i]
                elif answer[cur] + graph[cur][i] < answer[i]:
                    answer[i] = answer[cur] + graph[cur][i]
        cur = getsmallest()

V, E = map(int, input().split())
start = int(input())
data = [list(map(int, input().split())) for _ in range(V)]

graph = [['INT']*(V+1)]
for i in range(1, V+1):
    row = ['INT'] * (V+1)
    row[i] = 0            
    graph.append(row)

for item in data:
    graph[item[0]][item[1]] = item[2]

answer = graph[start]
visited = [False]* (V+1)
visited[0] = True

solution()

for i in range(1,V+1):
    print(answer[i])

