t = int(input())
l = []

for i in range(t):
    a, b = input().split()
    a = int(a)
    c = ''
    for j in range(len(b)):
        c += b[j] * a
    l.append(c)

for x in l:
    print(x)
    
    