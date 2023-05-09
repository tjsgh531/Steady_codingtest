import math

# 최소공배수 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

# 입력받기
for i in range(3):
    a, b = map(int, input().split())
    print(lcm(a, b))
