# [0] 변수 선언
hour, minute = input().split()
hour, minute = int(hour), int(minute)


# [1] 조건 비교 후 값 할당 
if(0 <= minute < 45):
    minute += 15    
    if(0 < hour <= 23):
        hour -= 1
    else:
        hour = 23  

else:
    minute -= 45


# [2] 출력 
print(hour, minute)
