n = int(input())
core = list(map(int, input().split()))
max_core = max(core)
sum = 0

for i in core:
    i = i / max_core * 100
    sum += i

print(sum / n)