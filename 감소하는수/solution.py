N = int(input())

def solution():
    one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    two = [10, 20, 21, 30, 31, 32, 40, 41, 42, 43, 50, 51, 52]
    three = [210, 321, 320, 310, 432, 431, 430, 421, 420, 410]
    cnt = 10
    maxnum = 9876543210
    
    if N < cnt:
        return answer[N]

    while 1:
        for i in range(1, 10):
            cnt += i
            if cnt > 
