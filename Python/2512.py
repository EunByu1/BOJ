# 이분 탐색 PS
import sys

input = sys.stdin.readline
N     = int(input())
req   = list(map(int, input().split()))
M     = int(input())


# [1] 범위 설정
lo  = 0
hi  = max(req)
mid = (lo + hi) // 2
ans = 0

# [2] 정부 예산 넘기는지 확인
def is_possible(mid):
    return sum(min(mid, r) for r in req) <= M

# [3] 이분 탐색 반복 실행
while lo <= hi :
    if is_possible(mid):
        lo  = mid + 1
        ans = mid

    else:
        hi  = mid - 1

    mid = (lo + hi) // 2

print(ans)
