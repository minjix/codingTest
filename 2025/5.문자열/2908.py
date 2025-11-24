a, b = input().split()
c = []
c.append(int(a[::-1]))
c.append(int(b[::-1]))
print(max(c))