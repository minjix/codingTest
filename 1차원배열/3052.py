l = []

for _ in range(10):
    n = int(input())
    l.append(n % 42)
        
result = list(set(l))
print(len(result))
