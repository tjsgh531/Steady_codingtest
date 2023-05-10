import math
import sys

input = sys.stdin.readline

n = int(input())
trees = [int(input()) for i in range(n)]

distances = [0]*(n-1)
for i in range(1, n):
    distances[i-1] = trees[i] - trees[i-1]

gcd_value = distances[0]
for j in range(1, n-1):
    gcd_value = math.gcd(gcd_value, distances[j])

total_length = 0
for k in range(n-1):
    total_length += distances[k]

num_trees = (total_length//gcd_value) + 1 - n

print(num_trees)
