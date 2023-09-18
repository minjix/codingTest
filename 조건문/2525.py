A, B = map(int, input().split())
C = int(input())

if((B+C)> 60):
    A = A + ((B+C) // 60)
    if(A > 23):
        A -= 24
    B = ((B+C) % 60)
    if(B > 59):
        B -= 60
else:
    A = A + ((B+C) // 60)
    if(A > 23):
        A -= 24
    B = B+C
    if(B > 59):
        B -= 60

print(A, B)