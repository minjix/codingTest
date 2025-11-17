sumList = []

while True:
    try:
        a, b = map(int, input().split())
        sumList.append(a + b)
    except EOFError:
        break

for x in sumList:
    print(x)
