# [0] 데이터 입력 후 테스트 케이스(T)에 할당
T         = int(input())
A         = 0
B         = 0
Store_A   = []
Store_B   = []
Store_Cal = []

# [1] 테이스 케이스(T)의 값에 따라, 입력 후 연산 실행 -> 저장 
for i in range(T):
    A, B = map(int, input().split())
    Store_A.append(A)
    Store_B.append(B)
    Store_Cal.append(A + B)
    
# [2] 저장된 값을 이용하여  "Case #x: A + B = C" 형식으로 출력
for i in range(T):
    print("Case #%d: %d + %d = %d" % (i+1, Store_A[i], Store_B[i], Store_Cal[i]))
