# 백준 9461

n = int(input())
num = [int(input()) for _ in range(n)]

semo = [0,1,1,1,2,2,3,4,5,7,9]

for i in range(11, 101):
    semo.append(semo[i-2] + semo[i-3])

for x in num:
    print(semo[x])
