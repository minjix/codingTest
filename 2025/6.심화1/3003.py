total = [1, 1, 2, 2, 2, 8]

now = list(map(int, input().split()))
s = []

for i in range(len(total)):
    s.append(total[i] - now[i])

print(*s)