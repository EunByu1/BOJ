import heapq as hq
import sys

pq = []
for _ in range(int(sys.stdin.readline())):
    value = int(sys.stdin.readline())

    if value != 0:
        hq.heappush(pq, (abs(value), value))

    else:
        print(hq.heappop(pq)[1] if pq else 0)
