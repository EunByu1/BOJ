# [방법_1]
tri_size = int(input())
tri_list = []

for _ in range(tri_size):
    tri_list.append(list(map(int, input().split())))

# DP를 위한 리스트 초기화
dp_list = [[0]*tri_size for _ in range(tri_size)]
dp_list[0][0] = tri_list[0][0]

# DP를 통한 최대 합 계산
for i in range(1, tri_size):
    for j in range(i+1):
        # 맨 왼쪽 요소
        if j == 0:
            dp_list[i][j] = dp_list[i-1][j] + tri_list[i][j]
        # 맨 오른쪽 요소
        elif j == i:
            dp_list[i][j] = dp_list[i-1][j-1] + tri_list[i][j]
        # 중간 요소
        else:
            dp_list[i][j] = max(dp_list[i-1][j-1], dp_list[i-1][j]) + tri_list[i][j]

# 마지막 행에서 최대값 출력
print(max(dp_list[tri_size-1]))




# [방법_2]
tri_size = int(input())
tri_list = []
dp_list  = []

for _ in range(tri_size):
    tri_list.append(list(map(int, input().split())))

dp_list.append([tri_list[0][0]])

for i in range(1, tri_size):
    dp_value_list = []
    for j in range(i + 1):  # 삼각형의 i번째 행은 i+1개의 요소를 가집니다
        # 맨 왼쪽 요소
        if j == 0:
            dp_value = dp_list[i-1][0] + tri_list[i][j]
        # 맨 오른쪽 요소
        elif j == i:
            dp_value = dp_list[i-1][j-1] + tri_list[i][j]
        # 중간 요소
        else:
            dp_value = max(dp_list[i-1][j-1], dp_list[i-1][j]) + tri_list[i][j]
        dp_value_list.append(dp_value)
    dp_list.append(dp_value_list)

print(max(dp_list[-1]))
