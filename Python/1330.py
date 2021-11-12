# [0] 값을 입력받은 후 변수에 할당함 
A,B = input().split(" ")

# [1] TypeCasting 
A = int(A)
B = int(B)

# [2] 조건에 맞게 값을 출력함
if ( A > B ) :
    print(">")
elif ( A < B ) :
    print("<")
else :
    print("==")
