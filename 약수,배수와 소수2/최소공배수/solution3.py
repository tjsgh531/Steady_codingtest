import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    

    for i in range(1, A+1):
        if A % i == 0 and B % i == 0:
            ans = i

    print(int(A * B / ans))