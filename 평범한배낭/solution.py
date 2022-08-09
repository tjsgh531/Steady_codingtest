N, K = map(int, input().split())
bag = []

for _ in range(N):
    w, v = map(int, input().split())
    bag.append((w, v))

dp = ['남은칸'][i]