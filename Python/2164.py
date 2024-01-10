# [방법 1] : 50924KB, 188ms
from collections import deque

T = int(input())
q = deque()
for i in range(1, T+1):
    q.append(i)


for _ in range(T-1):
    q.popleft()
    q.append(q[0])
    q.popleft()
    
print(q.popleft())



# [방법 2] : 50972KB, 208ms
from collections import deque
import sys

N  = int(sys.stdin.readline())
dq = deque(range(1, N+1))

while len(dq)>1 :
    dq.popleft()
    dq.append(dq.popleft())
    
print(dq.popleft())



# [방법 3] : 50924KB, 224ms
from collections import deque

N  = int(input())
dq = deque(range(1, N+1))

while len(dq)>1 :
    dq.popleft()
    dq.append(dq.popleft())
    
print(dq.popleft())
