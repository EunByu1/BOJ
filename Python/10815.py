# 이분 탐색 PS
# [방법 1]
from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
qry = list(map(int, input().split()))
ans = []

for q in qry:
    l = bisect_left(cards, q)
    r = bisect_right(cards, q)
    ans.append(1 if r-l > 0 else 0)

print(*ans)


# [방법 2]
from bisect import bisect_left

N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
qry = list(map(int, input().split()))
ans = []

for q in qry:
    l = bisect_left(cards, q)
    if l != len(cards) and cards[l] == q:
        ans.append(1)
    else:
        ans.append(0)
        
print(*ans)


# [방법 3]
import sys

input = sys.stdin.readline

N  = int(input())
Nc = sorted(list(map(int, input().split())))
M  = int(input())
Mc = list(map(int, input().split()))

for card in Mc:
    lo  = 0
    hi  = len(Nc) - 1
    mid = (lo+hi) // 2

    valid = False
    
    while lo <= hi:
        if card == Nc[mid]:
            valid = True
            break
        else:    
            if card > Nc[mid] :
                lo = mid + 1
            elif card < Nc[mid] :
                hi = mid - 1
        mid = (lo + hi) // 2
        
    if valid:
        print(1, end=" ")
    else:
        print(0, end=" ")
