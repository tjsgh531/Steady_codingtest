import sys
input = sys.stdin.readline

a = [[] for _ in range(51)]

N = int(input())

for _ in range(N):
    temp = input()
    a[len(temp)].append(temp)

for wordlist in a:
    if wordlist:
        for word in sorted(set(wordlist)):
            print(word, end='')

# 런타임 에러
# https://www.acmicpc.net/problem/1181