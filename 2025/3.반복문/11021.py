n = int(input())
sumList = []

for _ in range(n):
    a, b = map(int, input().split())
    sumList.append(a+b)

for j in range(1, n + 1):
    print("Case #{0}: {1}".format(j, sumList[j-1]))