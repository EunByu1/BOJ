# [0] 값을 저장할 변수 선언 
Store = []
Count = 0   


# [1] 입력 후 연산 & 저장
while(1):
    A, B = map(int, input().split())
    Store.append(A+B)

    if (Store[Count] == 0):
        break
    Count += 1
Count = 0


# [2] 저장된 값 출력
while(1):
    if(Store[Count] == 0):
        break

    print(Store[Count])
    Count += 1
    

