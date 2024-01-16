# Greedy Algorithm
N, L = map(int, input().split())
coord = [False] * 1001
for i in map(int, input().split()):
    coord[i] = True

ans = 0 # 테이프 개수
x   = 0 # 포인트 역할

while (x < 1001) :
    if coord[x]:
        ans += 1
        x += L
    else:
        x += 1
        
print(ans)
