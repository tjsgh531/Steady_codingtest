a, b, c, d, e, f = map(int, input().split())

if a ==0:
    y = int(c / b)
    x = int((b * f - c * e)/(b * d))
else:        
    y = int((a * f - d * c) / (a * e - d * b))
    x = int(c/a - (b*y)/a)

print(f"{x} {y}")
