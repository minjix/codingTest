n = int(input())
a = []
b = []

for _ in range(n):
    x,y = map(int, input().split())
    a.append(x)
    b.append(y)

for i in range(0, n):
    print("Case #{0}: {1} + {2} = {3}".format(i+1,a[i], b[i], a[i]+b[i]))