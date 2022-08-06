import sys

Input = []

for i in range(3):
    Input.append(int(sys.stdin.readline()))
    
Input = str(Input[0] * Input[1] * Input[2])

for i in range(10):
    print(Input.count(str(i)))
