import sys
input = sys.stdin.readline

def check(n):
    for i in range(3, n, 2):
        if n % i == 0:
            n += 2
            return check(n)
    return n

N = int(input())
for _ in range(N):
    n = int(input())

    if n == 0 or n == 1:
        print(2)
        continue

    if n % 2 == 0:
        n += 1

    print(check(n))
# 시간 초과

# dp 로 풀면 안되나?


        