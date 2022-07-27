import sys
input = sys.stdin.readline

3-2
2
3
2+3
3+3-2
3+3
3+3+3-2
2+3+3
3+3+3
3+3+3+2

def solution():
    global answer
    for i in marbles:
        answer[i] = 'Y'

N = int(input())
weights = list(map(int, input().split()))
T = int(input())
marbles = list(map(int, input().split()))
total = sum(marbles)
answer = ['N'] * (total+1)