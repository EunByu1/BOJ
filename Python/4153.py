import sys

while(1):
    value = list(map(int, sys.stdin.readline().split()))
    value.sort()

    if (value[0] == value[1] == value[2] == 0):
        break


    if ((value[2] ** 2) == (value[0] ** 2) + (value[1] ** 2)):
        print("right")
    else:
        print("wrong")
