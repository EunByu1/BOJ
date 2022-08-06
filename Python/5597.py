import sys

students_O = []
students_X = []

for i in range(28):
    students_O.append(int(sys.stdin.readline()))

for j in range(30):
    tmp = students_O.count(j+1)

    if (tmp == 0):
        students_X.append(j+1)

students_X.sort(reverse=False)
print(students_X[0])
print(students_X[1])
