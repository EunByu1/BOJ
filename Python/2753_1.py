# [0] 변수 선언
year = int(input())

# [1] 조건 비교 및 출력
if ( ( year % 4 ) == 0 ) :
    if ( (year % 100 ) != 0 ) :
        print("1")
    elif ( ( year % 400 ) == 0 ) :
        print("1")
    else :
        print("0")
else :
    print("0")
