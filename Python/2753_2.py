# 재귀 함수 ver.

# [0] 변수 선언
year = int(input())

# [1] 함수 선언 및 정의 
def Leap_year_1(year_V1):
    if ( year_V1 == 0 ):
        return 1
    elif ( year_V1 < 0 ):
        return 0
    else :
        return Leap_year_1(year_V1 - 4) 

# [2] 함수 호출
LeapYear = Leap_year_1(year)

# [3] 조건 비교 및 출력
if ( LeapYear == 0 ) :
    print(0)
else :
    if ( ( year % 100) != 0 ) or ( (year % 400) == 0 ):
        print(1)
    else:
        print(0)



        
