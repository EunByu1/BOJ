import sys

def verification(ver):
    Sum = 0
    for i in ver:
        Sum += i**2
        
    return Sum % 10

num = list(map(int, sys.stdin.readline().split()))
print(verification(num))
