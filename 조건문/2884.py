H, M = map(int, input().split())

if(H == 0):
    if(M >= 45):
        M -=45
    else:
        H = 23
        M = 60 - 45 + M
else:
    if(M >= 45):
        M -=45
    else:
        H -= 1
        M = 60 - 45 + M

print(H , M)