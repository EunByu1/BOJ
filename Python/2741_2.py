# RecursionError #

# [0] 데이터 입력
user = int(input())
user_list = []

# [1] 첫째 줄부터 N번째 줄 까지 차례대로 빈 리스트에 저장 
def N(User):
    if (User == 1):
        user_list.append(User)
        return user_list
    else :
        user_list.append(User)
        return N(User-1)


# [2] 함수 호출 후 할당 
Final_value = N(user)


# [3] 리스트에 저장된 값 출력
for i in Final_value[::-1]:
    print(i)
