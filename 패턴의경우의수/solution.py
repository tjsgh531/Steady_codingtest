import copy

def printpattern(pattern):
    for row in pattern:
        for item in row:
            print(item, end='\t')
        print()
    return "--------------------------"

def init(start):
    pattern = [[0] * 3 for _ in range(3)]
    pattern[start[0]][start[1]] = 1
    return pattern

def connect(pattern, current, n):
    global answer
    for i in range(3):
        for j in range(3):
            cur_n = n
            dup_pattern = copy.deepcopy(pattern)
            if dup_pattern[i][j] == 1:
                continue
            if (current[0] + i) % 2 == 0 and (current[1] + j) % 2 == 0:
                if dup_pattern[(current[0]+i)//2][(current[1]+j)//2] == 0:
                    continue
            dup_pattern[i][j] = 1
            cur_n -= 1
            if cur_n > 1:
                connect(dup_pattern, (i, j), cur_n)
            else:
                answer += 1
                print(f"answer  : {answer}")
                print(printpattern(dup_pattern) )
            
answer = 0
for i in range(3):
    for j in range(3):
        init_pattern = init((i,j))
        connect(init_pattern, (i,j), 4)
print(answer)