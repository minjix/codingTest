def returnOne(n):
    print(n)
    if n == 1:
        return
    if n % 2 == 0:
        returnOne(n // 2)
    else:
        returnOne(n*3 + 1)

returnOne(3)