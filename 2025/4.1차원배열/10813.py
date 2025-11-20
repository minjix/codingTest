n, m = map(int, input().split())
b = list(i for i in range(1, n+1))

for i in range(m):
    x, y = map(int, input().split())
    b[x-1], b[y-1] = b[y-1], b[x-1]
    
print(*b)