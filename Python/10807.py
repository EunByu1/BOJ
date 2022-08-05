import sys
T = sys.stdin.readline()
value = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(value.count(v))
