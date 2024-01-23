# BFS 최단경로 PS
from collections import deque
import sys

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
N, M  = map(int, input().split())
board = [input() for _ in range(N)]
input = sys.stdin.readline

# 범위(경로) 벗어났는지 확인
def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    dq = deque()
    # 칸을 셀 때에는 시작 위치와 도착 위치도 포함
    dq.append((0, 0, 1))    
 
    while dq:
        y, x, d = dq.popleft()

        # 마지막 좌표에 도달할 경우
        if (y == N-1) and (x == M-1):
            return d

        nd = d + 1
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))
                
print(bfs())
