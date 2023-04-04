import sys
input = sys.stdin.readline

a = [[] for _ in range(51)]
N = int(input())
for _ in range(N):
    temp = input()
    a[len(temp)].append(temp)

for wordlist in a:
    if len(wordlist) != 0:
        for word in sorted(set(wordlist)):
            print(word)

#런타임 에러 : indexError