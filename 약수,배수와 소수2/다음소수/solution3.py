import sys
import math
input = sys.stdin.readline

N = int(input())

num = set()
num.add(2)


def check(n):
    if n in num:
        return n
    
    for i in num:
        # 소수가 아님
        if n % i == 0:
            return check(n+2)


for _ in range(N):
    n = int(input())
    if n == 0 or n == 1:
        print(2)
        continue

    if n % 2 == 0:
        n += 1
    
    temp = max(num)
    if n > temp:
        for i in range(temp+2, n+1, 2):
            num.add(check(i))
    
    print(check(n))

        