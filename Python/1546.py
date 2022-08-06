import sys

num      = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_max  = max(num_list)
num_sum  = 0

for i in num_list:
    num_sum += (i/num_max*100)

print(num_sum / num)
