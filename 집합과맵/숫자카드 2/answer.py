import sys
from collections import Counter

input = sys.stdin.readline
# 입력 받기
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

# 각 숫자 카드의 개수 구하기
card_count = Counter(cards)
print(card_count)
print(type(card_count))
# 찾고자 하는 숫자가 몇 개 있는지 출력
for number in numbers:
    print(card_count[number], end=" ")
