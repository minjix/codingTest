l = list()
for i in range(9):
    a = int(input())
    l.append(a)

m = max(l)
n = l.index(m)+1

print(m)
print(n)