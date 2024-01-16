# Greedy Algorithm
import sys

N, K  = map(int, input().split())
input = sys.stdin.readline
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0

for coin in coins:
    ans += K // coin
    K %= coin
    
print(ans)
