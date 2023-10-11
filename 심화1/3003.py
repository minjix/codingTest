a,b,c,d,e,f = map(int, input().split())

num = []
num.append(1-a)
num.append(1-b)
num.append(2-c)
num.append(2-d)
num.append(2-e)
num.append(8-f)

print(*num)
