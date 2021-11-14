# [0] 값을 입력받고, TypeCasting 후 변수에 할당함
x = int(input())
y = int(input())

# [1] 조건에 맞게 값을 출력
if (( x > 0 ) & ( y > 0 )):
    print(1)
elif (( x > 0 ) & ( y < 0 )):
    print(4)
elif (( x < 0 ) & ( y > 0 )):
    print(2)
else:
    print(3)
