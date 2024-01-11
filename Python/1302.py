# [방법 1]
import sys
input = sys.stdin.readline
name  = []
book  = []
count = []

for _ in range(int(input())):
    book.append(input())

name = set(book)

for i in name:
    count.append((book.count(i), i))

count.sort(key=lambda x: (-x[0], x[1]))
print(count[0][1])

# [방법 2] : 자료구조 map(dictionary) 활용
d = dict()

for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

m = max(d.values())
candi = []

for k,v in d.items():
    if v == m:
        candi.append(k)

candi.sort()
print(candi[0])
