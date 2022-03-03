# [0] 변수 선언부 
user  = input()
cal_1 = user
count = 0

# [1] 10보다 작을 경우 앞에 0을 붙여 두 자리 수로 재구성 
if(int(user) < 10):
    user  = '0' + user
    cal_1 = '0' + cal_1

# [2] 연산 수행     
while(1):
    cal_2 = str(int(cal_1[0]) + int(cal_1[1]))

    if(int(cal_2) < 10):
        cal_2 = '0' + cal_2

    cal_1 = cal_1[1] + cal_2[1]
    count += 1

    if(user == cal_1):
        print(count)
        break
