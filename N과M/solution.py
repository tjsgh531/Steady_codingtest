def dfs(cur, k):
    if len(cur) >= M:
        answer.append(cur)
        return

    for i in range(k, N+1):
        dup_cur = cur[:]
        dup_cur.append(i)
        dfs(dup_cur, i)

N, M = map(int, input().split())
answer =[]
init_cur = []

dfs(init_cur, 1)
for ans_list in answer:
    for item in ans_list:
        print(item, end=' ')
    print()