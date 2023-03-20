def solution(n, s):
    answer = []
    if n > s:
        answer.append(-1)
        return answer
    if s % n == 0:
        for _ in range(n):
            answer.append(s//n)
        return answer
    else:
        for _ in range(n - (s%n)):
            answer.append(s//n)
        for _ in range(s%n):
            answer.append(s//n + 1)
        return answer