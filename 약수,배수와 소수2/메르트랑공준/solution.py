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

while True:
    num = int(input())
    if num == 0:
        break

    cnt = 0
    for i in range(num+1, num*2 +1):
        if i % 2 == 0:
            continue
        if isPrime(i):
            cnt += 1
    print(cnt)
# 시간초과