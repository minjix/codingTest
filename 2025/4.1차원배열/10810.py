n, m = map(int, input().split())

b = ([0 for i in range(n)])

for i in range(m):
    x, y, z = map(int, input().split())

    for j in range(x-1, y):
        b[j] = z   

print(*b)