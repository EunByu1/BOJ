# [Top-down]
import sys

sys.setrecursionlimit(10 ** 7)
MOD = 10_007
cache = [0] * (1000 + 1)

def tile(n):
    if cache[n]:
        return cache[n]

    if (n == 0) or (n == 1):
        cache[n] = 1
    else:
        cache[n] = tile(n-1) + tile(n-2)
        cache[n] %= MOD

    return cache[n]

print(tile(int(input())))


# [Bottom-up]
MOD = 10_007
n = int(input())
cache = [-1] * (n + 1)
cache[0] = cache[1] = 1

for i in range(2, n+1):
    cache[i] = cache[i-1] + cache[i-2]
    cache[i] %= MOD

print(cache[n])
