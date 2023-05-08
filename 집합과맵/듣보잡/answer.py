import sys
input = sys.stdin.readline
# 듣지 못한 사람의 명단 입력 받기
n, m = map(int, input().split())
hear = set()
for i in range(n):
    hear.add(input().strip())

# 보지 못한 사람의 명단 입력 받기
see = set()
for i in range(m):
    see.add(input().strip())

# 듣보잡 명단 구하기
intersection = sorted(list(hear & see))

# 결과 출력
print(len(intersection))
for name in intersection:
    print(name)
