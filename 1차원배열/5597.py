student = [i for i in range(1, 31)]

for _ in range(28):
    s = int(input())
    i = student.index(s)
    del student[i]

student.sort()

for i in range(len(student)):
    print(student[i])

