import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

# b 와 d의 최소 공배수 = 분모
lcm = b * d // math.gcd(b, d)

#분자 구해야죠
numerator = a * (lcm // b) + c * (lcm // d)

# 기약 분수로 만들어야죠
gcd = math.gcd(lcm, numerator)

print(numerator//gcd, lcm//gcd)