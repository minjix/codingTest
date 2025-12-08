# # 동적 계획법
# def fibonachi(num):
#     if num <= 1:
#         return num
#     return fibonachi(num-1) + fibonachi(num-2)
# print(fibonachi(9))

def fibo(n):
    cache = [0 for i in range(n + 1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2, n+1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]

print(fibo(4))