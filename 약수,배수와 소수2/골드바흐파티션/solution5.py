import sys
input = sys.stdin.readline

isprime = [0] * 1000001
primes = []

for i in range(2, 1000001):
    if isprime[i] == 0:
        primes.append(i)
        for j in range(i*2, 1000001, i):
            isprime[j] = 1

T = int(input())
for _ in range(T):
    n = int(input())

    cnt = 0
    for i in primes:
        if i <= n:
            break
        if not isprime[n-i] and i <= n-i:
            cnt += 1
    print(cnt)