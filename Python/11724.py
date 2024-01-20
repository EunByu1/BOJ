import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
adj  = [[0] * N for _ in range(N)]

for _ in range(M):
    # 코드는 0부터 시작이고, 문제는 1부터 시작이므로 (a-=1 & b-=1)
    a, b = map(lambda x: x-1, map(int, input().split()))
    
    # 무방향(=양방향)
    adj[a][b] = adj[b][a] = 1
    
def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

ans = 0
chk = [False] * N

for i in range(N):
    # 방문하지 않았다면 (=체크되지 않았다면)
    if not chk[i]:
        ans += 1
        dfs(i)

print(ans)
