import math
import sys
input = sys.stdin.readline

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) +1 ):
        if num % i == 0:
            return False
    return True

primes = [1] * 1000001

for i in range(2, 1000001):
    if primes[i] == 1 and isPrime(i):
        for j in range(i*2, 1000001, i):
            primes[j] = 0
    
T = int(input())
for _ in range(T):
    n = int(input())

    cnt = 0
    for i in range(2, n//2 +1):
        if primes[i] + primes[n-i] == 2:
            cnt += 1

    print(cnt)
