# [0] 연산한 값을 저장할 변수 선언 
Store    = []

# [1] 연산 후 저장
while(1):
    try:
        A, B  = map(int, input().split())
        Store.append(A+B)
    except:
        break
    
# [2] 저장된 값 출력 
for T in Store:
    print(T)
