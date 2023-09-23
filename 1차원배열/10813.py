N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    a = basket[i-1]
    b = basket[j-1]

    temp = b
    basket[j-1] = a
    basket[i-1] = temp
    temp = 0

print(*basket)
