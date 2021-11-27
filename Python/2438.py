# [0] 데이터 입력
StarNum = int(input())

# [1] 첫째 줄부터 N번째 줄까지 차례대로 별을 출력
for N in range(StarNum):
    Star = "*" * (N+1)
    print(Star)
