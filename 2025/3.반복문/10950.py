a = int(input())

l = list()

for i in range(a):
    b,c = map(int, input().split())
    l.append(b+c)

for j in l:
    print(j)