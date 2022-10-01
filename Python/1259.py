import sys

while(1):
  value = sys.stdin.readline().strip()

  if(value == "0"):
    break
  
  if(value == value[::-1]):
    print("yes")
  else :
    print("no")
