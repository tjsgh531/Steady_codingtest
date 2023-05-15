import math
import sys

input = sys.stdin.readline

def is_prime(num):
    if num < 2:  # 0과 1은 소수가 아님
        return False

    # 2부터 제곱근까지의 숫자로 나누어보며 소수인지 판별
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

# 입력 받기
m, n = map(int, input().split())

# 범위 내에서 소수 출력
for i in range(m, n + 1):
    if is_prime(i):
        print(i)