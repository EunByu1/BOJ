import sys

A, B    = map(int,sys.stdin.readline().split())
list_A  = []
list_B  = []
Sum     = ""

for i in range(A):
    list_A.append(list(map(int, sys.stdin.readline().split())))

for i in range(A):
    list_B.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(list_A)):
    for j in range(B):
        Sum = Sum + str(list_A[i][j] + list_B[i][j]) + " "

    print(Sum)
    Sum = ""
