import sys

List = []
for i in range(10):
    num = int(sys.stdin.readline()) % 42
    
    if (List.count(num) == 0):
        List.append(num)
    else:
        pass

print(len(List))
