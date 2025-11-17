a, b = map(int, input().split())
sumList = []

while not(a == 0 and b == 0):
    sumList.append(a + b)
    x, y = map(int, input().split())
    a = x
    b = y

for i in sumList:
    print(i)