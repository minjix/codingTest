N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    l = basket[i-1:j]
    l.reverse()
    basket[i-1:j] = l

print(*basket)
    