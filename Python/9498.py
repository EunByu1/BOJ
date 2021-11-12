# [0] 성적 값을 입력 받음
score = int(input())

# [1] 조건에 맞게 값을 출력함
if (score >= 90):
    print("A")
elif (score >= 80):
    print("B")
elif (score >= 70):
    print("C")
elif (score >= 60):
    print("D")
else:
    print("F")
