# [0] 데이터 입력
N,X = map(int, input().split())
A   = input().split()

# [1] X보다 작은 수 출력
for i in A:
    if int(i) < X:
        print(i, end=" ")
