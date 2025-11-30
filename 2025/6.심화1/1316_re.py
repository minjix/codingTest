n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    seen = []
    isGroup = True
    
    for i in range(len(word)):
        ch = word[i]
        
        if ch not in seen:
            seen.append(ch)
        else:
            if word[i-1] != ch:
                isGroup = False
                break

    if isGroup:
        cnt += 1

print(cnt)

