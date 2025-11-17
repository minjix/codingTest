import sys

#n = int(input())
n = int(sys.stdin.readline())
sumList = list()

for _ in range(n):
    #a, b = map(int, input().split())
    a, b = map(int, sys.stdin.readline().split())
    sumList.append(a + b)

for j in sumList:
    print(j)