def solution():
    for i in range(1, N+1):
        answer[i] = min(answer[i], answer[i-1] +1)
        if i % 3 == 0:
            answer[i] = min(answer[i], answer[i//3] + 1)
        if i % 2 == 0:
            answer[i] = min(answer[i], answer[i//2] + 1)
        print(f"i : {i} \t answer : {answer}")

N = int(input())
answer = list(range(N+1))
solution()
print(answer[-1])
