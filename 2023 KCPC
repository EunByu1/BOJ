import sys 

value_list = ['K', 'O', 'R', 'E', 'A']
user  = sys.stdin.readline()
count = 0
index = 0

# 검사 코드 
for i in user:
  # value_list 범위 넘어감 == KOREA 문자열 완성
  if(index == len(value_list)):
    index = 0

  # 같으면 카운트
  if(value_list[index] == i):
    count = count + 1
    index = index + 1
    
    
print(count)
