from queue import Empty
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    s = list(map(int, input().split()))
    s2 = []
    result = 0
    
    while len(s) > 0:
        temp = s.pop()
        while(len(s2) > 0 and s2[-1] < temp): 
            s2.pop()
        if(len(s2) == 0):
            s2.append(temp)
        else :
            result += s2[-1] - temp
    print(result)