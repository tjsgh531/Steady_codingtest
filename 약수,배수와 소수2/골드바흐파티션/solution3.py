import sys
import math

input = sys.stdin.readline

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

T = int(input())
for _ in range(T):
    n = int(input())
    
    cnt = 0
    for i in range(2, n//2+1):
        if  isPrime(i) and isPrime(n-i):
            cnt += 1
    print(cnt)
