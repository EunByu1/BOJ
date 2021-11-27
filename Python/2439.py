# [0] 데이터 입력
StarNum = int(input())
Vacuum  = 'T'

# [1] 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
for n in range(1, StarNum+1):
    Star = 'T' * (StarNum - n) + '*' * n
    print(Star.replace('T',' '))

