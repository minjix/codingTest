core = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
grade = ["A+", "A0", "B+", "B0", "C+", "C0", "D+","D0","F"]

total = 0
result = 0

# 다시 해보기!!!
for _ in range(20):
    s, p ,g = input().split()
    p = float(p)

    if g != "P":
        total += p
        result += p * core[grade.index(g)]

print('%6f' % (result/total))