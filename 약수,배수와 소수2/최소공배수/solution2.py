import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    ans = 1

    if A > 1:
        for i in range(2, A+1):
            if A % i == 0 and B % i == 0:
                ans *= i
                A = int(A/i)
                B = int(B/i)
    print(ans * A * B)