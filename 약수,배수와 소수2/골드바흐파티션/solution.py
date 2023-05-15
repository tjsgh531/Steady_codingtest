import sys
import math
input = sys.stdin.readline

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

prime_dic = [0] * 1000001
prime_dic[2] = 1

for i in range(2, 1000001):
    if isPrime(i):
        prime_dic[i] = 1

T = int(input())

for _ in range(T):
    n = int(input())
    
    cnt = 0
    for i in range(2, n//2+1):
        if prime_dic[i] == 1:
            if prime_dic[n-i] == 1:
                cnt+=1

    print(cnt)
# 시간초과