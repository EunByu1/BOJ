# [0] 데이터 입력
T     = int(input())
Store = []

# [1] 테스트 케이스의 개수만큼 입력 & 연산 후 저장
for TestCase in range(T):
    A, B = map(int, input().split())
    Store.append(A+B)

# [2] 저장된 값 출력
for TestCase in range(T):
    print("Case #%d: %d" % (TestCase+1, Store[TestCase]))
    
