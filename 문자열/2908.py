a, b = input().split()

c =""
d = ""
for i in range(3):
    c += a[3-i-1]
    d += b[3-i-1]

if int(c) > int(d):
    print(c)
else:
    print(d)

