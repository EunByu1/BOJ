a, b     = map(int, input().split())
multiply = a * b

# 최대공약수[GCD]
while(a % b != 0):
  c = a % b
  a = b
  b = c  
GCD = b

# 최소공배수[LCM]
LCM = int(multiply / b)

# 출력: 최대공약수[GCD] & 최소공배수[LCM] 
print(GCD)
print(LCM)
