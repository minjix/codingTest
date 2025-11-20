n = int(input())

res = []

for _ in range(n):
    s = input()
    res.append(s[0] + s[-1])

for i in res:
    print(i)