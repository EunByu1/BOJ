# [0] 테스트 케이스의 개수 입력
TestCase = int(input())


# [1] 연산 후 값 저장할 리스트 생성
Store = []


# [2] 테스트 케이스의 개수만큼 값 입력&연산 후 저장
for i in range(TestCase):
    A, B = input().split()
    A, B = int(A), int(B)
    
    Store.append(A+B)


# [3] 저장된 값 출력
for i in range(TestCase):
    print(Store[i])
