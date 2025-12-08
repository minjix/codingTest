# 백준 11726

n = int(input())

if n == 1:
    print(1)
else:
    nemo = [0 for i in range(n+1)]
    nemo[1] = 1
    nemo[2] = 2

    for i in range(3, n+1):
        nemo[i] = (nemo[i-1] + nemo[i-2]) % 10007

    print(nemo[n])