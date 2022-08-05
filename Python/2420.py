# [0] 모듈 import 및 입력 
import sys
N, M= map(int, sys.stdin.readline().split())

# [1] 절댓값 함수를 이용한 절댓값 출력 
print(abs(N-M))
