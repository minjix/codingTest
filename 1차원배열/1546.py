N = int(input())

core = list(map(int, input().split()))

m = max(core)

sum = float()

for i in range(len(core)):
    sub = core[i]/m*100
    core[i] = sub

    sum += core[i]

print(sum/len(core))

