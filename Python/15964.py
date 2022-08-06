import sys

def A_B(A, B):
    return ((A + B) * (A - B))

A, B = map(int, sys.stdin.readline().split())
print(A_B(A, B))
