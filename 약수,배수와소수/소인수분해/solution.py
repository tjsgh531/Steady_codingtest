N = int(input())

while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)
                N =int(N/i)
                break

