n, x = map(int, input().split())
l = list(map(int, input().split()))

a = list()

for i in l:
    if i < x:
        a.append(i)

print(*a)
