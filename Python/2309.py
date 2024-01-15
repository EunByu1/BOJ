# [완전 탐색 문제]
from itertools import combinations
import sys

heights = []
input = sys.stdin.readline

for i in range(9):
    heights.append(int(input()))

for combi in combinations(heights, 7):
    if sum(combi) == 100:
        for height in sorted(combi):
            print(height)
      # 꼭 넣어줘야 함!    
        break
