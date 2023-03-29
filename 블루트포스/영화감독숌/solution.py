N = int(input())

# 666 1666 2666 3666 4666 5666 6660 6661 6662 6663

idx = 0
count = 0
while(count != N):
    if idx % 10 != 6:
        temp = idx*1000 + 666
        count += 1
        if count == N:
            print(temp)
    else:
        cnt = 1
        temp = idx
        while (temp % 10 == 6):
            cnt *= 10
            temp = int(temp/10)
        
        temp = int((idx*1000+666)/cnt)*cnt
        for i in range(cnt):
            count+=1
            if count == N:
                print(temp+i)
                break
    idx+=1