import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    if n <= 2:
        print(2)
        continue
    if n % 2 == 0:
        n += 1

    while True:
        for i in range(3, n, 2):
            if n % i == 0:
                n += 2
                break
        else:
            print(n)
            break
# 시간 초과
