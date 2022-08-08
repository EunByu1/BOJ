import sys

x, y, w, h = map(int, sys.stdin.readline().split())

length_1 = x
length_2 = w - x
length_3 = y
length_4 = h - y

print(min(length_1, length_2, length_3, length_4))
