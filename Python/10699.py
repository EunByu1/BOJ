# [0] 날짜/시간 모듈 import
import datetime

# [1] 날짜/시간 정보 가져옴 -> format
day = datetime.datetime.now()
tmp = day.strftime("%Y-%m-%d")

# [2] 출력 
print(tmp)
