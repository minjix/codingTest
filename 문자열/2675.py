n = int(input())

for i in range(n):
    R, S = input().split()
    R = int(R)
    for j in S:
        print(j*R, end="")
    print()
