n, x = map(int, input().split())

num = list(map(int, input().split()))
c = []

for i in num:
    if i < x:
        c.append(i)

print(*c)