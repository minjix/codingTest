a = []

for row in range(9):
    row = list(map(int, input().split()))
    a.append(row)

m = []
for row in range(9):
    for col in range(9):
        m.append(int(a[row][col]))

max_res = max(m)

print(max_res)

for row in range(9):
    for col in range(9):
        if int(a[row][col]) == max_res:
            print(row+1, col+1, end=" ")