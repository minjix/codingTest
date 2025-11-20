num = set()

for _ in range(10):
    a = int(input())
    num.add(a % 42)

print(len(num))