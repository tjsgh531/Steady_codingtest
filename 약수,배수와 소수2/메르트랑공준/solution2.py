import sys
import math
input = sys.stdin.readline

def isPrime(num):
    for i in range(3, int(math.sqrt(num)) + 1 , 2):
        if num % i == 0:
            return False
    return True

prime_dic = [0]* (123456*2+1)
prime_dic[2] = 1

for i in range(3, 123456*2+1, 2):
    if isPrime(i):
        prime_dic[i] = 1

while True:
    num = int(input())
    if num == 0:
        break
    
    cnt = 0
    for i in range(num + 1, num*2 +1):
        if prime_dic[i] == 1:
            cnt+= 1
    print(cnt)
        