T = int(input())

for _ in range(T):
    n = int(input())
    
    s = [] # n이하 소수
    for num in range(2, n):
        
        #num이 소수 인지 아닌지 판단
        if num % 2 == 0:
            continue
        for i in range(3, num, 2):
            if num % i == 0:
                break
        else:
            s.append(num)

    ans = []
    for i in s:
        if i > n/2:
            break
        if n-i in s:
            ans = [i, n-i]
    
    print(f"{ans[0]} {ans[1]}")

        