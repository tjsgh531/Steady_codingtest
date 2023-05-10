import math
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

#b 와 d의 최소공배수 = 분모를 구해야 한다.
lcm = (b * d) // math.gcd(b, d)

#분자 구해야지
ans = a * (lcm//b) + c * (lcm//d)

print(f"{ans} {lcm}")