A = [[0 for _ in range(100)]  for _ in range(100)]

num = int(input())
for _ in range(num):
    a, b = map(int, input().split(' '))
    for row in range(b-1, b+9):
        for col in range(a-1, a+9):
            A[row][col] = 1
sumvalue = 0
for i in A:
    sumvalue += sum(i)
print(sumvalue)